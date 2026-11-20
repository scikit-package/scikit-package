import subprocess
from pathlib import Path
from urllib.parse import quote

import requests
from cookiecutter.config import get_user_config
from cookiecutter.exceptions import CookiecutterException
from cookiecutter.repository import expand_abbreviations

from scikit_package.utils import io, pypi


def run(repo_url, update=False):
    """Run cookiecutter with optional config file."""
    username_or_orgname = repo_url.split("/")[3]
    repo_name = repo_url.split("/")[4]
    tag = io.get_latest_release_tag(username_or_orgname, repo_name)
    _check_cookiecutter(repo_url, tag)
    if repo_name == "scikit-package-conda-forge":
        package_name = input(
            "Enter the package name to check whether it's available on PyPI: "
        )
        pypi.check_pypi_package_exists(package_name)
    print(f"> The latest release version of {tag} of {repo_name} is used.")
    try:
        cmd = ["cookiecutter", repo_url]
        cmd.extend(["--checkout", tag])
        config_cmd = io.get_config_cmd()
        if update:
            config_cmd.extend(["_is_skpkg_update=Yes"])
        else:
            config_cmd.extend(["_is_skpkg_update=No"])
        cmd.extend(config_cmd)
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run scikit-package for the following reason: {e}")


def _check_cookiecutter(repo_url, tag):
    """Check the cached template and saved project configuration."""
    owner, repo = repo_url.split("/")[3:5]

    try:
        config = get_user_config(
            config_file=(
                str(io.config_file) if io.config_file.exists() else None
            )
        )
        reference = expand_abbreviations(repo_url, config["abbreviations"])

        if reference == repo_url:
            template_dir = Path(config["cookiecutters_dir"]) / repo
        else:
            candidates = [
                Path(reference),
                Path(config["cookiecutters_dir"]) / reference,
            ]
            template_dir = next(
                (
                    path
                    for path in candidates
                    if (path / "cookiecutter.json").is_file()
                ),
                None,
            )
            if template_dir is None:
                raise ValueError(
                    "Cannot verify the configured template override. "
                    "Use the official repository URL or a local "
                    "Git checkout."
                )

        if template_dir.exists():
            _check_template_release(template_dir, owner, repo, tag)

        response = requests.get(
            f"https://raw.githubusercontent.com/{owner}/{repo}/"
            f"{quote(tag, safe='')}/cookiecutter.json",
            timeout=10,
        )
        response.raise_for_status()
        _check_project_config(response.json())

    except (
        CookiecutterException,
        OSError,
        ValueError,
        requests.RequestException,
        subprocess.CalledProcessError,
    ) as error:
        raise SystemExit(f"Error: {error}") from None


SCHEMA_KEY = "_skpkg_schema_version"


def _check_template_release(template_dir, owner, repo, tag):
    """Check the selected template against the requested release."""
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/commits/"
        f"{quote(tag, safe='')}",
        timeout=10,
    )
    response.raise_for_status()
    expected_commit = response.json()["sha"]

    actual_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=template_dir,
        text=True,
    ).strip()
    changes = subprocess.check_output(
        ["git", "status", "--porcelain"],
        cwd=template_dir,
        text=True,
    ).strip()

    if actual_commit != expected_commit or changes:
        raise ValueError(
            f"The template at {template_dir} is not a clean checkout "
            f"of release {tag}. For a cached template, rerun and accept "
            "the re-download. For a local template override, select "
            "a clean checkout of that release."
        )


def _check_project_config(template):
    """Check saved settings against the released template."""
    expected_version = template.get(SCHEMA_KEY)

    if not io.proj_config_file.exists():
        return expected_version

    settings = io.read_skpkg_config(io.proj_config_file)
    if not isinstance(settings, dict):
        raise ValueError("cookiecutter.json must contain a JSON object.")

    if expected_version is None and SCHEMA_KEY not in settings:
        return

    unsupported = sorted(set(settings) - set(template))
    if unsupported:
        raise ValueError(
            "cookiecutter.json contains unsupported fields: "
            f"{', '.join(unsupported)}. Update these settings to the "
            "current format before continuing."
        )

    actual_version = settings.get(SCHEMA_KEY)
    if actual_version != expected_version:
        raise ValueError(
            "Your cookiecutter.json is incompatible with the current "
            "scikit-package template. Please update this file to match "
            "the latest supported configuration format and try again."
        )

    return expected_version
