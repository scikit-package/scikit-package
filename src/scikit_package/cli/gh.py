import json
import os
import re
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlparse

import requests
import yaml
from requests.exceptions import JSONDecodeError

from scikit_package.utils.io import get_config_value


def broadcast_issue_to_repos(args):
    """Broadcast a GitHub issue to multiple repositories."""
    source_repo_url, issue_content = _get_issue_content(args.issue_url)
    groups_dict, repos_dict = _get_broadcast_repos_dict(args.url_to_repo_info)
    broadcast_urls = _get_broadcast_urls(
        args.group_name, groups_dict, repos_dict
    )
    if source_repo_url in broadcast_urls:
        print("Excluding the source repository from the broadcast list.")
        broadcast_urls.remove(source_repo_url)
    gh_token = os.environ.get("GITHUB_TOKEN", None)
    if gh_token is None:
        raise EnvironmentError(
            "GITHUB_TOKEN environment variable is not set. "
            "Please set it to a valid GitHub token with "
            "permissions to create issues in the target repositories."
        )
    dry_run = True
    dry_run = not (args.dry_run == "n")
    return _broadcast_issue_to_urls(
        issue_content,
        broadcast_urls,
        gh_token,
        dry_run,
    )


def _get_issue_content(issue_url):
    """Fetch the contents of the issue that will be broadcast.

    Parameters
    ----------
    issue_url: str
      url to the issue to be broadcast. Currently it takes the form:
      https://github.com/{user-or-org-name}/{repo-name}/issues/{issue-number}

    Returns
    -------
    source_repo_url: str
        used to exclude source repo from the broadcasting target list.
    issue_content: dict
        issue-title and issue-body to be broadcast.
    """
    parsed = urlparse(issue_url)
    path_parts = parsed.path.strip("/").split("/")
    try:
        owner = path_parts[0]
        repo = path_parts[1]
        issue_number = int(path_parts[3])
    except (IndexError, ValueError):
        raise ValueError(
            f"{issue_url} is not a valid url to be parsed. "
            "Please ensure the input url is with a format like "
            "https://github.com/username/reponame/issues/issue-number"
        )
    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    )
    source_repo_url = f"https://github.com/{owner}/{repo}"
    try:
        response = requests.get(api_url)
        assert response.status_code == 200
        issue_content = response.json()
    except (AssertionError, requests.JSONDecodeError):
        raise ValueError(
            f"Can not find the corresponding issue from {issue_url}. "
            "Please ensure the input url is with a format like https://"
            "github.com/username/reponame/issues/issue-number"
        )
    return source_repo_url, issue_content


def _get_broadcast_repos_dict(url_to_repo_info=None):
    """Load the repos database and the groups database and return them
    as dictionaries.

    Take ``url_to_repo_info`` as a pointer to the databases as input.
    Currently supported is that this can point to a folder on the filesystem
    or a URL to a GitHub repository.  If the former is passed, it is
    expected to find ``repos.json`` or ``repos.yaml`` and ``groups.json`` or
    ``groups.yaml`` in the folder.  If the latter, the two files should be
    in the top level of the git repository.

    If ``url_to_repo_info`` is None, use the current working directory. If
    the files are not found in the current working directory, look for a
    valid the ``url_to_repo_info`` in the users scikit-package run-control
    config file at ``~/.skpkgrc``.

    If ``url_to_repo_info`` is a valid URL it is assumed that it points to a
    GitHub repository, otherwise it is assume it is a valid file-path
    reference.

    Parameters
    ----------
    url_to_repo_info : str. Optional. Default is None.
        The pointer to the location where the database files may be found that
        contain the lists of repository URLs (``repos.json``, ``repos.yaml``)
        and broadcast groups (``groups.json``, ``groups.yaml``).

        ``url_to_repo_info`` could point to a folder on the file-system that
        contains the two files, or to a GitHub/GitLab repository that
        contains the two files at the top level. ``url_to_repo_info`` is
        optional. If it is not specified, package will look in the current
        working directory for the files. If it doesn't find both there it will
        look in the user's ``~/.skpkgrc`` configuration file.

    Returns
    -------
    groups_dict : dict
        The dictionary that maps group names to lists of repo names.
        It looks like
        {"odd_repos": ["repo1", "repo3"], "even_repos": ["repo2"]}.
    repos_dict : dict
        The dictionary that maps repo names to their URLs.
        It looks like
        {
            "repo1":  "https://github.com/myorg/myrepo1",
            "repo2":  "https://github.com/myorg/myrepo2",
            "repo3":  "https://github.com/myorg/myrepo3"
        }
    """

    def _load_json_or_yaml_from_dir(dir_path: Path, file_stems: list):
        extensions = [".json", ".yaml", ".yml"]
        return_dict = {}
        find_all = []
        for file_stem in file_stems:
            find_file = False
            for ext in extensions:
                file_path = dir_path / f"{file_stem}{ext}"
                if file_path.is_file():
                    find_file = True
                    with open(file_path, "r") as f:
                        if ext == ".json":
                            return_dict[file_stem] = json.load(f)
                        elif ext == ".yaml":
                            return_dict[file_stem] = yaml.safe_load(f)
                    break
            find_all.append(find_file)
        find_all = all(find_all)
        return return_dict, find_all

    def _load_json_or_yaml_from_repo(repo_url, file_stems):
        with TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            subprocess.run(
                ["git", "clone", repo_url, str(tmp_path)],
                capture_output=True,
                text=True,
            )
            return _load_json_or_yaml_from_dir(tmp_path, file_stems)

    def is_github_repo_url(url: str) -> bool:
        pattern = re.compile(
            r"^(https://github\.com/|git@github\.com:|git://github\.com/)"
            r"([\w.-]+)/([\w.-]+)(\.git)?/?$"  # owner/repo
        )
        return bool(pattern.match(url))

    def _check_dicts(groups_dict, repos_dict):
        repos_mentioned = set(
            [value for _, values in groups_dict.items() for value in values]
        )
        for repo_name in repos_mentioned:
            if repo_name not in repos_dict:
                raise KeyError(
                    f"repo `{repo_name}` in the groups dictionary does not "
                    f"exist in repos dictionary {repos_dict.keys()}. "
                    "Please ensure all repo names in the groups dictionary "
                    "exist in the repos dictionary."
                )
        return groups_dict, repos_dict

    if url_to_repo_info:
        if url_to_repo_info.startswith(
            "http://"
        ) or url_to_repo_info.startswith("https://"):
            if not is_github_repo_url(url_to_repo_info):
                raise ValueError(
                    f"{url_to_repo_info} "
                    "is recognized as an url but it is not a valid url "
                    "to be parsed. Please ensure the input url is with a "
                    "format like "
                    "https://github.com/user-or-orgname/reponame "
                    "or provide a directory path instead."
                )
            dicts, find_all = _load_json_or_yaml_from_repo(
                url_to_repo_info,
                ["groups", "repos"],
            )
            if not find_all:
                raise FileNotFoundError(
                    f"{url_to_repo_info} "
                    "is a valid GitHub repository URL but the required "
                    "files `groups.json`(or `groups.yaml`), "
                    "`repos.json`(or `repos.yaml`) do not exist in the "
                    "repository. Please ensure both files exist in the "
                    "top level of the GitHub repository."
                )
            return _check_dicts(dicts["groups"], dicts["repos"])
        else:  # url_to_repo_info is a directory path
            path = Path(url_to_repo_info)
            if not path.is_dir():
                raise NotADirectoryError(
                    f"The provided {url_to_repo_info} is recognized as a "
                    "local directory, but it doesn't exist. Please ensure it"
                    "exists on your local file system or provide a GitHub "
                    "repository URL instead."
                )
            dicts, find_all = _load_json_or_yaml_from_dir(
                path, ["groups", "repos"]
            )
            if not find_all:
                raise FileNotFoundError(
                    (
                        "The required files `groups.json`(or `groups.yaml`), "
                        "`repos.json`(or `repos.yaml`) do not exist in the "
                        f"directory {url_to_repo_info}. Please ensure both "
                        "files exist in the top level of the directory."
                    )
                )
            else:
                return _check_dicts(dicts["groups"], dicts["repos"])
    else:  # url_to_repo_info is None
        url_to_repo_info = Path().cwd()
        dicts, find_all = _load_json_or_yaml_from_dir(
            url_to_repo_info, ["groups", "repos"]
        )
        if find_all:
            return _check_dicts(dicts["groups"], dicts["repos"])
        else:
            try:
                url_to_repo_info = get_config_value(
                    "url_to_repo_info", Path().home() / ".skpkgrc"
                )
            except KeyError:
                raise KeyError(
                    "Can not find the required entry `url_to_repo_info` in "
                    "the directory specified in `~/.skpkgrc`. Please ensure "
                    "that either the current working directory or the "
                    "directory specified in `~/.skpkgrc` contains the "
                    "required files when `url_to_repo_info` is not provided "
                    "to the command."
                )
            return _get_broadcast_repos_dict(url_to_repo_info)


def _get_broadcast_urls(input_name, groups_dict, repos_dict):
    """Build the list of repository URLs from the repos and groups
    databases and a user-supplied group key.

    Parameters
    ----------
    input_name : str
        The user-supplied group key.
        For example, "even_repos".
    groups_dict : dict
        The dictionary that maps group names to lists of repo names.
        It looks like
        {"odd_repos": ["repo1", "repo3"], "even_repos": ["repo2"]}.
    repos_dict : dict
        The dictionary that maps repo names to their URLs.
        It looks like
        {
            "repo1":  "https://github.com/myorg/myrepo1",
            "repo2":  "https://github.com/myorg/myrepo2",
            "repo3":  "https://github.com/myorg/myrepo3"
        }

    Returns
    -------
    broadcast_urls : list of str
        The list of repo urls to broadcast the issue.
    """
    if input_name not in groups_dict:
        raise KeyError(
            f"The input name `{input_name}` does not exist in the "
            f"groups dictionary {groups_dict.keys()}. "
            "Please ensure the input name exists in the groups dictionary"
        )
    repo_names = groups_dict[input_name]
    broadcast_urls = []
    for repo_name in repo_names:
        broadcast_urls.append(repos_dict[repo_name])
    return broadcast_urls


def _broadcast_issue_to_urls(issue_content, repo_urls, gh_token, dry_run=True):
    """Broadcast a issue to multiple GitHub repositories.

     Parameters
    ----------
    issue_content : dict
        The issue_content needed to create issues in each repo.
    repo_urls : list of str
        The urls to the target repos.
    gh_token : str
        GitHub token for authentication.

    Returns
    -------
    non_gh_urls: list of str
        The list of non-GitHub repo urls.
    failed_gh_urls: list of str
        The list of GhitHub repo urls where issue creation failed.
    dry_run: bool
        Whether it is in dry-run mode.
    """
    data = {
        "title": issue_content["title"],
        "body": issue_content["body"],
    }
    headers = {
        "Authorization": f"token {gh_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    non_gh_urls = []
    for i in range(len(repo_urls)):
        try:
            api_url = _get_api_url(repo_urls[i])
        except (IndexError, AssertionError):
            non_gh_urls.append(repo_urls[i])
    repo_urls = [url for url in repo_urls if url not in non_gh_urls]
    if dry_run:
        might_fail_gh_urls_info = []
        might_succeed_gh_urls = []
        for i in range(len(repo_urls)):
            api_url = _get_api_url(repo_urls[i], endpoint="repo")
            response = requests.get(api_url)
            try:
                assert response.status_code == 200
                assert response.json().get("owner", False)
                might_succeed_gh_urls.append(repo_urls[i])
            except (AssertionError, JSONDecodeError):
                might_fail_gh_urls_info.append((repo_urls[i], response))
    else:
        failed_gh_urls_info = []
        success_gh_urls = []
        for i in range(len(repo_urls)):
            api_url = _get_api_url(repo_urls[i], endpoint="issues")
            response = requests.post(api_url, json=data, headers=headers)
            if response.status_code != 201:
                failed_gh_urls_info.append((repo_urls[i], response))
            else:
                success_gh_urls.append(repo_urls[i])
    if dry_run:
        _print_dry_run_message(
            non_gh_urls,
            might_fail_gh_urls_info,
            might_succeed_gh_urls,
        )
        might_fail_gh_urls = [url for url, _ in might_fail_gh_urls_info]
        return non_gh_urls, might_fail_gh_urls, dry_run
    else:
        _print_no_dry_run_message(
            non_gh_urls, failed_gh_urls_info, success_gh_urls
        )
        failed_gh_urls = [url for url, _ in failed_gh_urls_info]
        return non_gh_urls, failed_gh_urls, dry_run


def _get_api_url(repo_url, endpoint="issues"):
    """Get the GitHub API URL for a given repository URL and endpoint.

    Parameters
    ----------
    repo_url : str
        The URL of the target GitHub repository.
    endpoint : {"issues", "repo"}, str, optional
        The API endpoint to access. Default is "issues".

    Returns
    -------
    api_url : str
        The GitHub API URL for posting issues.
    """
    assert repo_url.startswith("https://github.com/")
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip("/").split("/")
    owner = path_parts[0]
    repo = path_parts[1]
    if endpoint == "issues":
        api_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    elif endpoint == "repo":
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
    else:
        raise ValueError(f"Unsupported endpoint: {endpoint}")
    return api_url


def _print_dry_run_message(
    non_gh_urls, might_fail_gh_urls_info, might_succeed_gh_urls
):
    print(
        "Dry-run mode: No issues will be created. "
        "To create issues, rerun with the '--dry-run n' option."
    )
    if len(non_gh_urls) > 0:
        print("The following non-GitHub repository URLs will be skipped:")
        for url in non_gh_urls:
            print(f"  - {url}")
    if len(might_fail_gh_urls_info) > 0:
        print(
            "Issue might fail to be created in the following GitHub "
            "repositories:"
        )
        for url, response in might_fail_gh_urls_info:
            print(f"  - [{response.status_code} {response.reason}] {url}")
    if len(might_succeed_gh_urls) > 0:
        print(
            "Issues would be created in the following GitHub " "repositories:"
        )
        for url in might_succeed_gh_urls:
            print(f"  - {url}")


def _print_no_dry_run_message(
    non_gh_urls, failed_gh_urls_info, success_gh_urls
):
    print("Dry-run mode disabled: Issues will be created. ")
    if len(non_gh_urls) > 0:
        print("The following non-GitHub repository URLs will be skipped:")
        for url in non_gh_urls:
            print(f"  - {url}")
    if len(failed_gh_urls_info) > 0:
        print("Failed to create issue in the following GitHub repositories:")
        for url, response in failed_gh_urls_info:
            print(f"  - [{response.status_code} {response.reason}] {url}")
    if len(success_gh_urls) > 0:
        print(
            "Successfully created issues in the following "
            "GitHub repositories:"
        )
        for url in success_gh_urls:
            print(f"  - {url}")
