def _get_broadcast_repos_dict(url_file_path=None):
    """Load the recognizable broadcast repository information from files
    in the given path or GitHub repo.

    If ``url_file_path`` is not None, first try to treat it as an URL, and if
    that fails, treat it as a directory path. If both fail, raise
    ``ValueError``. If ``url_file_path`` is None, the broadcast_url_file_path
    set in ``~/.skpkgrc`` will be used. If it is not found, use the current
    working directory as the ``url_file_path``.

    If the file ``groups.json`` and ``repos.json`` don't exist in
    ``url_file_path``, raise ``ValueError``.

    Parameters
    ----------
    url_file_path : str
        The file path or URL recognizable broadcast repository information.
        If it is None, the ``broadcast_url_file_path`` set in
        ``~/.skpkgrc`` will be used. If it is not found, use the current
        working directory as the ``url_file_path``.

    Returns
    -------
    broadcast_info_dict : dict
        The dict containing recognizable broadcast repo URLs.
    """
    broadcast_repos_dict = {}
    return broadcast_repos_dict


def _print_recognized_broadcast_repos(broadcast_repos_dict):
    """Print the recognized broadcast repository URLs from the dict.

    Parameters
    ----------
    broadcast_repos_dict : dict
        The dict containing recognizable broadcast repo URLs.
    """
    return None


def _get_broadcast_urls(selected_names, broadcast_repos_dict):
    """Get the urls and package names of all repositories to broadcast
    to.

    Parameters
    ----------
    selected_names : str
        The input string for selected_names. It takes the form:
        "repo1,repo2,group1"
    broadcast_repos_dict : dict
        The dict containing recognizable broadcast repo URLs.

    Returns
    -------
    broadcast_urls : list of str
        a list of repo urls to broadcast the issue.
    """
    broadcast_urls = []
    return broadcast_urls
