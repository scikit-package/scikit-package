import re
import shutil
import subprocess
from pathlib import Path

import click
import requests

from scikit_package.cli.create import SKPKG_GITHUB_URL
from scikit_package.utils import auth, cookie, io, pypi
from scikit_package.utils.shell import run

FEEDSTOCK_URL_TEMPLATE = (
    "https://github.com/conda-forge/{pkg_name}-feedstock.git"
)
RECIPE_FILE = "recipe/meta.yaml"
TOP_LEVEL_KEY_PATTERN = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):")
SHA256_PATTERN = re.compile(r"^(\s*(?:-\s+)?sha256:\s*)\S+")
SYMREF_PATTERN = re.compile(r"^ref:\s+refs/heads/(\S+)\s+HEAD", re.MULTILINE)


def _jinja_set_pattern(variable_name):
    """Build a pattern matching a '{% set <variable_name> = "..." %}'
    line."""
    return re.compile(
        rf"(\{{%-?\s*set\s+{variable_name}\s*=\s*)([\"'])[^\"']*\2(\s*-?%\}})"
    )


VERSION_SET_PATTERN = _jinja_set_pattern("version")
SHA256_SET_PATTERN = _jinja_set_pattern("sha256")


def _get_repo_slug(url):
    """Return the lowercase 'owner/repo' slug of a GitHub remote URL."""
    slug = re.sub(r"^(https://|git@)github\.com[:/]", "", url.strip())
    return re.sub(r"(\.git)?/?$", "", slug).lower()


def _update_meta_yaml(meta_file_path, new_version, new_sha256):
    """Update the version and source SHA256 in a feedstock meta.yaml.

    Only the SHA256 of the top-level ``source`` section is rewritten, so
    a recipe declaring several sources is never silently corrupted.
    """
    lines = io.read_file(meta_file_path)
    version_count = sha256_count = 0
    source_sha256_indices = []
    in_source_section = False
    for index, line in enumerate(lines):
        line, count = VERSION_SET_PATTERN.subn(
            rf"\g<1>\g<2>{new_version}\g<2>\g<3>", line
        )
        version_count += count
        line, count = SHA256_SET_PATTERN.subn(
            rf"\g<1>\g<2>{new_sha256}\g<2>\g<3>", line
        )
        sha256_count += count
        lines[index] = line
        section = TOP_LEVEL_KEY_PATTERN.match(line)
        if section:
            in_source_section = section.group(1) == "source"
        if in_source_section and SHA256_PATTERN.match(line):
            source_sha256_indices.append(index)
    if version_count == 0:
        raise ValueError(
            f"No '{{% set version = ... %}}' line was found in "
            f"{meta_file_path}. Please update the version and SHA256 in the "
            "recipe by hand and open the pull request manually."
        )
    if sha256_count == 0:
        if len(source_sha256_indices) != 1:
            raise ValueError(
                "Expected exactly one 'sha256:' entry under 'source:' in "
                f"{meta_file_path} but found {len(source_sha256_indices)}. "
                "Please update the version and SHA256 in the recipe by hand "
                "and open the pull request manually."
            )
        (index,) = source_sha256_indices
        lines[index] = SHA256_PATTERN.sub(rf"\g<1>{new_sha256}", lines[index])
    io.write_file(meta_file_path, lines)


def _check_gh_installed():
    """Refuse to continue when the GitHub CLI is unavailable."""
    if shutil.which("gh") is None:
        raise ValueError(
            "The GitHub CLI ('gh') was not found on your PATH but is "
            "required to open the pull request. Please install it by "
            "following https://github.com/cli/cli#installation, run "
            "'gh auth login', then re-run this command."
        )


def _check_working_tree_clean(cwd):
    """Refuse to continue when the feedstock clone has local changes."""
    changes = run(
        "git status --porcelain", cwd=cwd, capture_output=True
    ).stdout.strip()
    if changes:
        raise ValueError(
            f"The feedstock clone in {cwd} has uncommitted changes, which "
            "would be lost. Please commit them, or set them aside by running "
            "'git stash' in that directory, then re-run this command."
        )


def _check_branch_exists(cwd, branch_name):
    """Refuse to continue when the release branch already exists."""
    if run(
        f"git branch --list {branch_name}", cwd=cwd, capture_output=True
    ).stdout.strip():
        raise ValueError(
            f"The branch '{branch_name}' already exists in {cwd}. "
            f"Please delete it by running 'git branch -D {branch_name}' in "
            "that directory, then re-run this command."
        )


def _check_remote_exists(cwd, pkg_name):
    """Add the feedstock upstream remote, or verify the configured
    one."""
    feedstock_url = FEEDSTOCK_URL_TEMPLATE.format(pkg_name=pkg_name)
    remotes = run("git remote", cwd=cwd, capture_output=True)
    if "upstream" not in remotes.stdout.split():
        run(f"git remote add upstream {feedstock_url}", cwd=cwd)
        return
    actual_url = run(
        "git remote get-url upstream", cwd=cwd, capture_output=True
    ).stdout.strip()
    if _get_repo_slug(actual_url) != _get_repo_slug(feedstock_url):
        raise ValueError(
            f"The 'upstream' remote in {cwd} points to {actual_url} but "
            f"{feedstock_url} was expected. Please correct it by running "
            f"'git remote set-url upstream {feedstock_url}' in that "
            "directory, then re-run this command."
        )


def _get_upstream_default_branch(cwd):
    """Return the name of the default branch of the upstream feedstock.

    Feedstocks are not all on ``main``, so the branch is looked up on
    the remote rather than assumed.
    """
    try:
        symref = run(
            "git ls-remote --symref upstream HEAD",
            cwd=cwd,
            capture_output=True,
        ).stdout
    except subprocess.CalledProcessError:
        symref = ""
    match = SYMREF_PATTERN.search(symref)
    if not match:
        raise ValueError(
            f"The default branch of the upstream feedstock in {cwd} could "
            "not be determined. Please check your network connection and "
            "that 'git remote -v' lists a reachable 'upstream' remote, then "
            "re-run this command."
        )
    return match.group(1)


def _rollback(cwd, original_branch, branch_name, is_committed):
    """Return the feedstock clone to its original branch after a
    failure."""
    try:
        run(f"git checkout -- {RECIPE_FILE}", cwd=cwd)
        run(f"git checkout {original_branch}", cwd=cwd)
    except subprocess.CalledProcessError:
        print(
            f"\nThe feedstock clone in {cwd} could not be restored to "
            f"'{original_branch}'. Please inspect it by running 'git status' "
            "in that directory."
        )
        return
    if is_committed:
        print(
            f"\nThe branch '{branch_name}' in {cwd} still holds the release "
            "commit. Please push it and open the pull request by hand, or "
            f"discard it by running 'git branch -D {branch_name}'."
        )
        return
    try:
        run(f"git branch -D {branch_name}", cwd=cwd)
    except subprocess.CalledProcessError:
        pass


def _run_commands(cwd, meta_file_path, version, SHA256, username, pkg_name):
    """Create a PR from a branch name of <new_version> to the upstream
    default branch."""
    _check_working_tree_clean(cwd)
    _check_remote_exists(cwd, pkg_name)
    _check_branch_exists(cwd, version)
    default_branch = _get_upstream_default_branch(cwd)
    original_branch = auth.get_current_branch(cwd=cwd)
    is_committed = False
    try:
        run(f"git checkout {default_branch}", cwd=cwd)
        run(f"git pull upstream {default_branch}", cwd=cwd)
        run(f"git checkout -b {version}", cwd=cwd)
        _update_meta_yaml(meta_file_path, version, SHA256)
        run(f"git add {RECIPE_FILE}", cwd=cwd)
        try:
            run(f'git commit -m "release: update to {version}"', cwd=cwd)
        except subprocess.CalledProcessError:
            raise ValueError(
                f"There is nothing to commit because the recipe in {cwd} "
                f"already has version {version} and its SHA256. Please "
                "confirm the package has been released to PyPI, then re-run "
                "this command."
            )
        is_committed = True
        run(f"git push origin {version}", cwd=cwd)
        run(f"gh repo set-default conda-forge/{pkg_name}-feedstock", cwd=cwd)
        run(
            f"gh pr create --base {default_branch} "
            f"--head {username}:{version} --title 'Release {version}' ",
            cwd=cwd,
        )
    except Exception:
        _rollback(cwd, original_branch, version, is_committed)
        raise


def _list_feedstock(feedstock_path):
    """List all feedstocks in the feedstock directory."""
    if not Path(feedstock_path).is_dir():
        raise ValueError(
            f"The feedstock directory {feedstock_path} was not found. "
            "Please set 'feedstock_path' in your ~/.skpkgrc file to the "
            "directory holding your cloned feedstocks, then re-run this "
            "command."
        )
    feedstocks = sorted(
        path.name
        for path in Path(feedstock_path).iterdir()
        if path.is_dir() and path.name.endswith("-feedstock")
    )
    if not feedstocks:
        raise ValueError(
            f"No feedstocks found in {feedstock_path}. "
            f"Please ensure you have feedstocks cloned in {feedstock_path}."
        )
    return feedstocks


def _get_feedstock_choices(feedstock_path, feedstock_names):
    """Map each menu number to the PyPI release data of one feedstock.

    Feedstocks that cannot be resolved on PyPI are reported and skipped,
    so that one unresolvable feedstock does not block the others.
    """
    version_map = {}
    for feedstock_name in feedstock_names:
        pkg_name = feedstock_name.replace("-feedstock", "")
        try:
            pkg_pypi_data = pypi.get_pypi_version_sha(pkg_name, count=1)
            pkg_version, pkg_sha256 = next(iter(pkg_pypi_data.items()))
        except (ValueError, StopIteration, requests.RequestException):
            print(f"  -. {pkg_name}, skipped, no source distribution on PyPI")
            continue
        feedstock_dir_path = Path(feedstock_path) / feedstock_name
        i = len(version_map) + 1
        version_map[i] = {
            "package_name": pkg_name,
            "version": pkg_version,
            "sha256": pkg_sha256,
            "feedstock_dir_path": feedstock_dir_path,
            "meta_file_path": feedstock_dir_path / RECIPE_FILE,
        }
        print(f"  {i}. {pkg_name}, {pkg_version}, SHA256: {pkg_sha256[:5]}..")
    return version_map


def update_conda_forge():
    """Update the Python package version and SHA256 hash in a meta.yaml
    file, and create a pull request to the upstream feedstock
    repository.

    Step-by-step process:
    - List the latest versions and SHA256 hashes from PyPI.
    - Prompt the user to select the feedstock to update.
    - Update the meta.yaml file with the new version and SHA256 hash.
    - Commit and push the changes to a <username>/<version> branch on GitHub.
    - Create a pull request to the upstream feedstock default branch.
    - Prompt the user to use the pull request template via the CLI.

    The feedstock clone must have no uncommitted changes, because the
    release branch is created from the upstream default branch. If any
    step fails, the clone is returned to the branch it started on.
    """
    _check_gh_installed()
    feedstock_path = io.get_config_path_value("feedstock_path")
    feedstock_names = _list_feedstock(feedstock_path)
    print("Available feedstocks with the latest PyPI version/SHA256:")
    version_map = _get_feedstock_choices(feedstock_path, feedstock_names)
    if not version_map:
        raise ValueError(
            f"None of the feedstocks in {feedstock_path} could be matched to "
            "a source distribution on PyPI. Please check that the feedstock "
            "directory names match their PyPI package names and that you are "
            "online, then re-run this command."
        )
    choice = click.prompt(
        "Enter the corresponding number of the feedstock you want to update",
        type=click.IntRange(1, len(version_map)),
    )
    selected = version_map[choice]
    username = auth.get_github_username()
    _run_commands(
        selected["feedstock_dir_path"],
        selected["meta_file_path"],
        selected["version"],
        selected["sha256"],
        username,
        selected["package_name"],
    )


def update(args):
    subcmd = args.subcommand
    if subcmd == "conda-forge":
        update_conda_forge()
    elif subcmd is None:
        cookie.run(SKPKG_GITHUB_URL, update=True)
