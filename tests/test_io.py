import json
import re
from pathlib import Path

import pytest

from scikit_package.utils.io import copy_all_files, get_config_path_value


@pytest.mark.parametrize(
    "configured_value, expected_path",
    [
        # Test that a configured path is expanded to an absolute path
        # C1: Leading ~, expect the home directory substituted
        ("~/dev/feedstocks", Path.home() / "dev" / "feedstocks"),
        # C2: Trailing separator, expect it dropped
        ("~/dev/feedstocks/", Path.home() / "dev" / "feedstocks"),
        # C3: Environment variable, expect its value substituted
        ("$SKPKG_TEST_ROOT/feedstocks", Path("/tmp/skpkg") / "feedstocks"),
        # C4: Already absolute, expect it unchanged
        (str(Path.home() / "feedstocks"), Path.home() / "feedstocks"),
    ],
)
def test_get_config_path_value(
    configured_value, expected_path, tmp_path, monkeypatch
):
    monkeypatch.setenv("SKPKG_TEST_ROOT", "/tmp/skpkg")
    config_path = tmp_path / ".skpkgrc"
    config_path.write_text(json.dumps({"feedstock_path": configured_value}))
    assert (
        get_config_path_value("feedstock_path", config_path) == expected_path
    )


# C1: Source dir and target dir exist. Some files exist in target have the
#  the same name as the files in source dir and exists_ok is set to be
#  True. Expect files exist in target are not overwritten and all other files
#  from the source dir are copied over.
# C2: Source dir and target dir exist. Target dir is inside source
#  dir and exists_ok is set to be True. Expect all other files in source
#  dir are copied to target dir and the files already exist inside target
#  dir before the copying are not changed.
def test_copy_all_files(user_filesystem):
    source_dir = user_filesystem / "package-dir"
    expected_files = {
        # files already exists in target dir
        ".git/COMMIT_EDITMSG": (
            "The file already exists in the new project\n"
            "skpkg: last commit message in skpkg-package\n"
        ),
        "docs/source/tutorial.rst": (
            "The file already exists in the new project\n"
            "The tutorial for skpkg-package.\n"
        ),
        # files only in source dir
        "README.rst": (
            "|Icon| |title|_\n"
            "===============\n"
            "\n"
            ".. |title| replace:: title of README.rst in skpkg-package\n"
        ),
        "docs/source/index.rst": (
            "#######\n"
            "|title|\n"
            "#######\n"
            "\n"
            ".. |title| replace:: title of skpkg-package documentation\n"
        ),
    }
    # files with duplicated name exist in target_dir
    target_dir = user_filesystem / "target-dir"
    copy_all_files(source_dir, target_dir, exists_ok=True)
    for file_name, file_content in expected_files.items():
        file_path = target_dir / file_name
        actual_content = file_path.read_text()
        expected_content = file_content
        assert actual_content == expected_content
    # target_dir is inside source_dir
    target_dir = source_dir / "target-dir-inside-package-dir"
    copy_all_files(source_dir, target_dir, exists_ok=True)
    for file_name, file_content in expected_files.items():
        file_path = target_dir / file_name
        actual_content = file_path.read_text()
        expected_content = file_content
        assert actual_content == expected_content


# C1: An non-existing source dir and an existing target dir.
#  Expect FileNotFoundError.
# C2: An empty source dir and an existing target dir.
#  Expect FlileNotFoundError.
# C3: Existing source dir and target dir, but there is a file with the same
#  name found in both dirs and exists_ok is set to be False.
#  Expect FileExistsError.
def test_copy_all_files_bad(user_filesystem):
    # non-existing source directory
    non_existing_source_dir = user_filesystem / "other-dir"
    assert not non_existing_source_dir.exists()
    package_dir = user_filesystem / "package-dir"
    with pytest.raises(
        FileNotFoundError,
        match=re.escape(
            "Unable to find the source directory: "
            f"{str(non_existing_source_dir)}."
        ),
    ):
        copy_all_files(non_existing_source_dir, package_dir)

    # empty source directory
    empty_source_dir = user_filesystem / "empty-source-dir"
    assert empty_source_dir.exists() and (not any(empty_source_dir.iterdir()))
    with pytest.raises(
        FileNotFoundError,
        match=re.escape(
            f"Source directory {str(empty_source_dir)} found "
            "but it contains no files."
        ),
    ):
        copy_all_files(empty_source_dir, package_dir)

    # a file with the same name found in both dirs and exists_ok=False.
    source_dir = user_filesystem / "package-dir"
    target_dir = source_dir / "target-dir-inside-package-dir"
    duplicate_names = ["COMMIT_EDITMSG", "tutorial.rst"]
    with pytest.raises(
        FileExistsError,
    ) as error:
        copy_all_files(source_dir, target_dir, exists_ok=False)
        actual_error_message = str(error.value)
        assert str(target_dir) in actual_error_message
        for name in duplicate_names:
            assert name in actual_error_message
