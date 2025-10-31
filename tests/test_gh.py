from types import SimpleNamespace

import pytest

from scikit_package.cli.gh import _broadcast_issue_to_urls, _get_issue_content


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
            "Please ensure the input url is with a format like "
            "https://github.com/username/reponame/issues/issue-number"
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
            "Please ensure the input url is with a format like "
            "https://github.com/username/reponame/issues/issue-number"
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


@pytest.mark.parametrize(
    (
        "broadcast_urls,expected_non_gh_urls,expected_failed_urls,"
        "dry_run, create_issue_return_value, called_mockers"
    ),
    [
        # C1: a list of target repo urls and dry_run is True.
        #   Expect non_gh_urls, failed_gh_urls to be empty, and only
        #   dry_run_mocker is called.
        (
            [
                "https://github.com/user-or-orgname/reponame1",
                "https://github.com/user-or-orgname/reponame2",
            ],
            [],
            [],
            True,
            SimpleNamespace(status_code=201),
            [
                "dry_run_mocker",
            ],
        ),
        # C2: a list of target repo urls, and dry_run is False.
        #   Expect non_gh_urls, failed_gh_urls to be empty, and only
        #   create_issue_mocker is called.
        (
            [
                "https://github.com/user-or-orgname/reponame1",
                "https://github.com/user-or-orgname/reponame2",
            ],
            [],
            [],
            False,
            SimpleNamespace(status_code=201),
            [
                "create_issue_mocker",
            ],
        ),
        # C3: One URL is not with a format of GH repo, another URL is with
        #   a format of GH repo but doesn't point to a valid GH repo,
        #   dry_run is True.
        #   Expect non empty non_gh_urls, empty failed_urls, and only
        #   dry_run_mocker is called.
        (
            [
                "https://not-github.com/user-or-orgname/reponame2",
                "https://github.com/nonexisting/nonexisting",
            ],
            ["https://not-github.com/user-or-orgname/reponame2"],
            [],
            True,
            SimpleNamespace(status_code=404),
            [
                "dry_run_mocker",
            ],
        ),
        # C3: One URL is not with a format of GH repo, another URL is with
        #   a format of GH repo but doesn't point to a valid GH repo,
        #   dry_run is False.
        #   Expect non empty non_gh_urls, empty failed_urls, and only
        #   create_issue_mocker is called.
        (
            [
                "https://not-github.com/user-or-orgname/reponame2",
                "https://github.com/nonexisting/nonexisting",
            ],
            ["https://not-github.com/user-or-orgname/reponame2"],
            ["https://github.com/nonexisting/nonexisting"],
            False,
            SimpleNamespace(status_code=404),
            [
                "create_issue_mocker",
            ],
        ),
    ],
)
def test_broadcast_issue_to_urls(
    mocker,
    broadcast_urls,
    expected_non_gh_urls,
    expected_failed_urls,
    dry_run,
    create_issue_return_value,
    called_mockers,
):
    create_issue_mocker = mocker.patch(
        "requests.post",
        return_value=create_issue_return_value,
    )
    dry_run_mocker = mocker.patch(
        "scikit_package.cli.gh._print_dry_run_message",
        return_value=None,
    )
    issue_content = {"title": "issue-title", "body": "issue-body"}
    actual_non_gh_urls, actual_failed_urls, actual_dry_run = (
        _broadcast_issue_to_urls(
            issue_content,
            broadcast_urls,
            gh_token="dummy_token",
            dry_run=dry_run,
        )
    )
    mockers = {
        "create_issue_mocker": create_issue_mocker,
        "dry_run_mocker": dry_run_mocker,
    }
    for mocker_name, mocker_instance in mockers.items():
        if mocker_name in called_mockers:
            assert mocker_instance.call_count >= 1
        else:
            mocker_instance.assert_not_called()
    assert set(actual_non_gh_urls) == set(expected_non_gh_urls)
    assert set(actual_failed_urls) == set(expected_failed_urls)
    assert actual_dry_run is dry_run
