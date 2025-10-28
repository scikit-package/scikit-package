from types import SimpleNamespace

import pytest

from scikit_package.cli.gh import _get_issue_content


def test_get_issue_content(mocker):
    # C1: a valid issue url. Expect the source_repo_url and
    #   issue content are returned.
    get_issue_mocker = mocker.patch(
        "requests.get",
        return_value=SimpleNamespace(
            status_code=200,
            json=lambda: {"title": "issue-title", "body": "issue-body"},
        ),
    )
    issue_url = "https://github.com/user-or-orgname/reponame/issues/1"
    expected_issue_content = {"title": "issue-title", "body": "issue-body"}
    expected_source_repo_url = "https://github.com/user-or-orgname/reponame"
    actual_source_repo_url, actual_issue_content = _get_issue_content(
        issue_url
    )
    get_issue_mocker.assert_called_once()
    assert actual_source_repo_url == expected_source_repo_url
    assert actual_issue_content == expected_issue_content


def test_get_issue_content_bad(mocker):
    # C1: a not valid url. Expect ValueError.
    issue_url = "non-valid-url"
    with pytest.raises(
        ValueError,
        match=(
            f"{issue_url} is not a valid url to be parsed. "
            "Please input the url of the issue to be broadcasted. "
            "Its format should be https://"
            "github.com/username/reponame/issues/issue-number"
        ),
    ):
        source_repo_url, issue_content = _get_issue_content(issue_url)

    # C2: a valid url but can not find the corresponding issue.
    #   Expect ValueError.
    get_issue_fail_mocker = mocker.patch(
        "requests.get",
        return_value=SimpleNamespace(
            status_code=404,
            json=lambda: {"message": "Not Found"},
        ),
    )
    issue_url = "https://github.com/nonexisting/nonexisting/issues/0"
    with pytest.raises(
        ValueError,
        match=(
            f"Can not find the corresponding issue from {issue_url}. "
            "Please ensure the input url is correct. "
            "Its format should be https://"
            "github.com/username/reponame/issues/issue-number"
        ),
    ):
        source_repo_url, issue_content = _get_issue_content(issue_url)
    get_issue_fail_mocker.assert_called_once()


def test_get_broadcast_repos_dict():
    # C1: an URL input, and JSON files exist in the GH repo.
    #   Expect the broadcast repos dict is returned.
    # C2: a directory input and JSON files exist in the directory.
    #   Expect the broadcast repos dict is returned.
    # C3: no input, cwd have `repos.json` and `groups.json`,
    #   `~/skpkgrc` have `broadcast_url_dir_path`.
    #   Expect the broadcast repos dict specified in the cwd is returned.
    # C4: no input, cwd does not have the files.
    #   `~/skpkgrc` have `broadcast_url_dir_path`.
    #   Expect the broadcast repos dict specified in the
    #   `broadcast_url_dir_path` is returned.
    assert False


def test_get_broadcast_repos_dict_bad():
    # C1: a URL that does not point to a valid GH repo. Expect ValueError.
    # C2: a directory input but JSON files do not exist in the directory.
    #   Expect FileNotFoundError.
    # C3: no input, cwd does not have `repos.json` and `groups.json`,
    #   `~/skpkgrc` does not have `broadcast_url_dir_path`.
    #   raise KeyError.
    assert False


def test_get_broadcast_urls_bad():
    # C1: input names does not exist in `groups_dict` or `repos_dict`.
    #   Expect KeyError.
    assert False
