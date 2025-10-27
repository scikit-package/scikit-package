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
    """Load the recognizable broadcast repository names and URLs from
    files in the given directory or GitHub repo.

    If ``url_to_repo_info`` is None, use the current working directory. If the
    files are not found in the current working directory, use
    the broadcast_url_dir_path set in ``~/.skpkgrc``. If it is not found,
    raise ``ValueError``.

    ``url_to_repo_info`` is first treated as an URL, and if that fails,
    then it is treated as a directory. If both fail, raise
    ``ValueError``.

    If the files ``groups.json`` and ``repos.json`` don't exist in
    ``url_to_repo_info``, raise ``FileNotFoundError``.

    Parameters
    ----------
    url_to_repo_info : str
        The pointer to the location where the database files may be found that
        contain the lists of repository URLs (``repos.json`` or ``repos.yaml``)
        and broadcast groups (``groups.json`` or ``groups.yaml``).
        ``repos.json`` takes the form:
        {
            "repo-name": "https://github.com/user-or-org-name/repo-name",
            ...
        }

        ``repos.yaml`` takes the form:
        repo-name : "https://github.com/user-or-org-name/repo-name"
        ...

        ``groups.json`` takes the form:
        {
            "group1-name": ["repo1-name", "repo2-name", "repo3-name"],
            ...
        }

        ``groups.yaml`` takes the form:
        group1-name:
          - repo1
          - repo2
          - repo3
        ...

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
        It looks like {"group1": ["repo1", "repo2"], "group2": ["repo3"]}.
    repos_dict : dict
        The dictionary that maps repo names to their URLs.
        It looks like {"repo1": "https://github.com/user-or-org-name/repo1"}
    """
    groups_dict = {}
    repos_dict = {}
    return groups_dict, repos_dict


def _get_broadcast_urls(input_names, groups_dict, repos_dict):
    """Get the urls and repo names of all repositories to broadcast to.

    Parameters
    ----------
    input_names : list of str
        The input list of the names of repos and groups to broadcast to.
        It takes the form: ["repo1","repo2","group1"]
    groups_dict : dict
        The dictionary that maps group names to lists of repo names.
        It looks like {"group1": ["repo1", "repo2"], "group2": ["repo3"]}.
    repos_dict : dict
        The dictionary that maps repo names to their URLs.
        It looks like {"repo1": "https://github.com/user-or-org-name/repo1"}

    Returns
    -------
    broadcast_urls : list of str
        The list of repo urls to broadcast the issue.
    """
    broadcast_urls = []
    return broadcast_urls
