from urllib.parse import urlparse

import requests


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
            "Please input the url of the issue to be broadcasted. "
            "Its format should be https://"
            "github.com/username/reponame/issues/issue-number"
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
            "Please ensure the input url is correct. "
            "Its format should be https://"
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

        ``repos.json`` takes the form:
        {
            "repo1":  "https://github.com/myorg/myrepo1",
            "repo2":  "https://github.com/myorg/myrepo2",
            "repo3":  "https://github.com/myorg/myrepo3"
        }
        ``repos.yaml`` takes the form:
        "repo1":  "https://github.com/myorg/myrepo1",
        "repo2":  "https://github.com/myorg/myrepo2",
        "repo3":  "https://github.com/myorg/myrepo3"
        ``groups.json`` takes the form:
        {
            "odd_repos": ["repo1", "repo3"],
            "even_repos": ["repo2]
        }
        ``groups.yaml`` takes the form:
        odd_repos:
          - repo1
          - repo3
        even_repos:
          - repo2

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
            "repo1": "https://github.com/user-or-org-name/repo1",
            "repo2":  "https://github.com/myorg/myrepo2",
            "repo3":  "https://github.com/myorg/myrepo3"
        }
    """
    groups_dict = {}
    repos_dict = {}
    return groups_dict, repos_dict


def _get_broadcast_urls(input_names, groups_dict, repos_dict):
    """Build the list of repository URLs from the repos and groups
    databases and a user-supplied group key.

    Parameters
    ----------
    input_names : str
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
            "repo1": "https://github.com/user-or-org-name/repo1",
            "repo2":  "https://github.com/myorg/myrepo2",
            "repo3":  "https://github.com/myorg/myrepo3"
        }

    Returns
    -------
    broadcast_urls : list of str
        The list of repo urls to broadcast the issue.
    """
    broadcast_urls = []
    return broadcast_urls
