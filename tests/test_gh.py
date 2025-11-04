import json
import os
import re
from pathlib import Path
from types import SimpleNamespace

import pytest

from scikit_package.cli.gh import (
    _broadcast_issue_to_urls,
    _get_broadcast_repos_dict,
    _get_broadcast_urls,
    _get_issue_content,
)


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


@pytest.mark.parametrize(
    (
        "url_to_repo_info, input_type, cwd_dir, expected_group_dict,"
        "expected_repos_dict"
    ),
    [
        # C1: an URL input, and JSON files exist in the GH repo.
        #   Expect the broadcast repos dict is returned.
        (
            "https://github.com/user-or-orgname/reponame",
            "url",
            "cwd_dir",
            {
                "odd_group": ["repo1", "repo3"],
                "even_group": ["repo2", "repo4"],
            },
            {
                "repo1": "https://github.com/user/repo1",
                "repo2": "https://github.com/user/repo2",
                "repo3": "https://github.com/user/repo3",
                "repo4": "https://github.com/user/repo4",
            },
        ),
        # C2: a directory input and JSON files exist in the directory.
        #   Expect the broadcast repos dict is returned.
        (
            "repo_info_dir_json",
            "dir",
            "cwd_dir",
            {
                "odd_group": ["repo1", "repo3"],
                "even_group": ["repo2", "repo4"],
            },
            {
                "repo1": "https://github.com/user/repo1",
                "repo2": "https://github.com/user/repo2",
                "repo3": "https://github.com/user/repo3",
                "repo4": "https://github.com/user/repo4",
            },
        ),
        # C3: a directory input and YAML files exist in the directory.
        #   Expect the broadcast repos dict is returned.
        (
            "repo_info_dir_yaml",
            "dir",
            "cwd_dir",
            {
                "odd_group": ["repo1", "repo3"],
                "even_group": ["repo2", "repo4"],
            },
            {
                "repo1": "https://github.com/user/repo1",
                "repo2": "https://github.com/user/repo2",
                "repo3": "https://github.com/user/repo3",
                "repo4": "https://github.com/user/repo4",
            },
        ),
        # C4: no input, cwd have `repos.json` and `groups.json`,
        #   `~/.skpkgrc` have `url_to_repo_info`.
        #   Expect the broadcast repos dict specified in the cwd is returned.
        (
            None,
            "none",
            "repo_info_dir_json",
            {
                "odd_group": ["repo1", "repo3"],
                "even_group": ["repo2", "repo4"],
            },
            {
                "repo1": "https://github.com/user/repo1",
                "repo2": "https://github.com/user/repo2",
                "repo3": "https://github.com/user/repo3",
                "repo4": "https://github.com/user/repo4",
            },
        ),
        # C5: no input, cwd does not have the files.
        #   `~/.skpkgrc` have `url_to_repo_info`.
        #   Expect the broadcast repos dict specified in the
        #   `url_to_repo_info` is returned.
        (
            None,
            "none",
            "empty-source-dir",
            {
                "small_group": ["repo1", "repo2"],
                "large_group": ["repo101", "repo102"],
            },
            {
                "repo1": "https://github.com/user/repo1",
                "repo2": "https://github.com/user/repo2",
                "repo101": "https://github.com/user/repo101",
                "repo102": "https://github.com/user/repo102",
            },
        ),
    ],
)
def test_get_broadcast_repos_dict(
    mocker,
    user_filesystem,
    url_to_repo_info,
    input_type,
    cwd_dir,
    expected_group_dict,
    expected_repos_dict,
):

    if input_type == "url":

        def mock_clone_repo(cwd, **kwargs):
            # already a temporary directory created by
            #   _get_broadcast_repos_dict
            source_dir = user_filesystem / "repo_info_dir_json"
            group_json_content = (source_dir / "groups.json").read_text()
            repos_json_content = (source_dir / "repos.json").read_text()
            target_dir = cwd[-1]
            with open(f"{target_dir}/groups.json", "w") as f:
                f.write(group_json_content)
            with open(f"{target_dir}/repos.json", "w") as f:
                f.write(repos_json_content)

        mocker.patch(
            "subprocess.run",
            side_effect=mock_clone_repo,
        )
    os.chdir(user_filesystem / cwd_dir)
    mocker.patch(
        "pathlib.Path.home",
        return_value=user_filesystem / "home_dir",
    )
    if input_type == "url":
        url_to_repo_info = url_to_repo_info
    elif input_type == "dir":
        url_to_repo_info = str(user_filesystem / url_to_repo_info)
    else:
        url_to_repo_info = None
    actual_group_dict, actual_repos_dict = _get_broadcast_repos_dict(
        url_to_repo_info=url_to_repo_info
    )
    assert actual_group_dict == expected_group_dict
    assert actual_repos_dict == expected_repos_dict


@pytest.mark.parametrize(
    "url_to_repo_info, error, error_msg",
    [
        # C1: a valid URL that does not point to a GH repo. Expect ValueError.
        (
            "https://not-github.com/user-or-orgname/reponame",
            ValueError,
            (
                "https://not-github.com/user-or-orgname/reponame "
                "is recognized as an url but it is not a valid url "
                "to be parsed. Please ensure the input url is with a format "
                "like https://github.com/user-or-orgname/reponame "
                "or provide a directory path instead."
            ),
        ),
        # C2: a URL input but JSON files do not exist in the GH repo.
        #  Expect FileNotFoundError.
        (
            "https://github.com/user-or-orgname/reponame",
            FileNotFoundError,
            (
                "https://github.com/user-or-orgname/reponame "
                "is a valid GitHub repository URL but the required files "
                "`groups.json`(or `groups.yaml`), "
                "`repos.json`(or `repos.yaml`) do not exist in the "
                "repository. Please ensure both files exist in the "
                "top level of the GitHub repository."
            ),
        ),
    ],
)
def test_get_broadcast_repos_dict_bad_url(
    mocker, url_to_repo_info, error, error_msg
):
    mocker.patch(
        "subprocess.run",
        return_value=None,
    )
    with pytest.raises(
        error,
    ) as excinfo:
        _get_broadcast_repos_dict(
            url_to_repo_info=url_to_repo_info,
        )
    assert error_msg in str(excinfo.value)


@pytest.mark.parametrize(
    (
        "url_to_repo_info,home_dir,  make_incorrect_dicts, "
        "make_incorrect_skpkg, error, expected_error_msg_parts "
    ),
    [
        # C1: a directory input but the directory does not exist.
        #   Expect NotADirectoryError.
        (
            "nonexisting-dir",
            "home_dir",
            False,
            False,
            NotADirectoryError,
            (
                "The provided ",
                "is recognized as a "
                "local directory, but it doesn't exist. Please ensure it"
                "exists on your local file system or provide a GitHub "
                "repository URL instead.",
            ),
        ),
        # C2: a directory input but groups.json does not exist in the
        #   directory. Expect FileNotFoundError.
        (
            "empty-source-dir",
            "home_dir",
            False,
            False,
            FileNotFoundError,
            (
                "The required files `groups.json`(or `groups.yaml`), "
                "`repos.json`(or `repos.yaml`) do not exist in the "
                "directory ",
                "Please ensure both files "
                "exist in the top level of the directory.",
            ),
        ),
        # C3: groups_dict and repos_dict are loaded but the some repo name
        #   in groups_dict does not exist in repos_dict. Expect KeyError.
        (
            "repo_info_dir_json",
            "home_dir",
            True,
            False,
            KeyError,
            (
                "repo `repo1` in the groups dictionary does not exist "
                "in repos dictionary ",
                "Please ensure all repo names in the groups dictionary "
                "exist in the repos dictionary.",
            ),
        ),
        # C4: no input, cwd does not have `repos.json` and `groups.json`,
        #   `~/.skpkgrc` does not have `repo_to_url_info`.
        #   Expect KeyError.
        (
            None,
            "another_home_dir",
            False,
            True,
            KeyError,
            (
                "Can not find the required entry `url_to_repo_info` in the "
                "directory specified in `~/.skpkgrc`. Please ensure that "
                "either the current working directory or the directory "
                "specified in `~/.skpkgrc` contains the required files when "
                "`url_to_repo_info` is not provided to the command.",
            ),
        ),
    ],
)
def test_get_broadcast_repos_dict_bad_dir(
    mocker,
    user_filesystem,
    url_to_repo_info,
    make_incorrect_dicts,
    make_incorrect_skpkg,
    home_dir,
    error,
    expected_error_msg_parts,
):
    mocker.patch(
        "pathlib.Path.home",
        return_value=user_filesystem / home_dir,
    )
    if make_incorrect_dicts:
        url_to_repo_info_path = user_filesystem / url_to_repo_info
        repos_json_file = url_to_repo_info_path / "repos.json"
        repos_dict = json.loads(repos_json_file.read_text())
        repos_dict.pop("repo1")
        with open(repos_json_file, "w") as f:
            json.dump(repos_dict, f)
    if make_incorrect_skpkg:
        skpkg_file = Path().home() / ".skpkgrc"
        with open(skpkg_file, "w") as f:
            json.dump({"url_to_repo_info": None}, f)
    if url_to_repo_info:
        url_to_repo_info = str(user_filesystem / url_to_repo_info)
    with pytest.raises(
        error,
    ) as excinfo:
        _get_broadcast_repos_dict(url_to_repo_info=url_to_repo_info)
    for msg_part in expected_error_msg_parts:
        assert msg_part in str(excinfo.value)


def test_get_broadcast_urls():
    # C1: input name is a group name.
    #   Expect the corresponding list of repo urls is returned.
    groups_dict = {
        "odd_group": ["repo1", "repo3"],
        "even_group": ["repo2", "repo4"],
    }
    repos_dict = {
        "repo1": "https://github.com/user/repo1",
        "repo2": "https://github.com/user/repo2",
        "repo3": "https://github.com/user/repo3",
        "repo4": "https://github.com/user/repo4",
    }
    input_name = "odd_group"
    expected_urls = [
        "https://github.com/user/repo1",
        "https://github.com/user/repo3",
    ]
    actual_urls = _get_broadcast_urls(
        input_name=input_name,
        groups_dict=groups_dict,
        repos_dict=repos_dict,
    )
    assert set(actual_urls) == set(expected_urls)


def test_get_broadcast_urls_bad():
    # C1: input name does not exist in `groups_dict` or `repos_dict`.
    #   Expect KeyError.
    input_name = "nonexisting_group"
    groups_dict = {"odd_group": ["repo1", "repo3"]}
    repos_dict = {
        "repo1": "https://github.com/user-or-orgname/reponame1",
        "repo3": "https://github.com/user-or-orgname/reponame3",
    }
    with pytest.raises(
        KeyError,
        match=re.escape(
            f"The input name `{input_name}` does not exist in the "
            f"groups dictionary {groups_dict.keys()}. "
            "Please ensure the input name exists in the groups dictionary"
        ),
    ):
        _get_broadcast_urls(
            input_name=input_name,
            groups_dict=groups_dict,
            repos_dict=repos_dict,
        )


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
        # C4: One URL is not with a format of GH repo, another URL is with
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
