import importlib
import re
from pathlib import Path

import pytest

from scikit_package.cli.update.conda_forge import (
    _get_repo_slug,
    _list_feedstock,
    _update_meta_yaml,
)


def test_update_meta_yaml_realistic(tmpdir):
    original_meta = """{%- set version = "1.0.5" -%}
package:
  name: {{ name|lower }}
  version: {{ version }}

source:
  url: https://pypi.org/packages/source/{{ name[0] }}/{{ name }}/{{ name }}-{{ version }}.tar.gz  # noqa: E501
  sha256: 1b71d398d73800db32b09785af0e7
"""
    new_version = "1.0.6"
    new_sha256 = "123456789abcdef0123456789"
    expected_updated_meta = """{%- set version = "1.0.6" -%}
package:
  name: {{ name|lower }}
  version: {{ version }}

source:
  url: https://pypi.org/packages/source/{{ name[0] }}/{{ name }}/{{ name }}-{{ version }}.tar.gz  # noqa: E501
  sha256: 123456789abcdef0123456789
"""
    meta_file = Path(tmpdir) / "meta.yaml"
    meta_file.write_text(original_meta)
    _update_meta_yaml(str(meta_file), new_version, new_sha256)
    updated_meta = meta_file.read_text()
    assert updated_meta == expected_updated_meta


@pytest.mark.parametrize(
    "original_meta, expected_updated_meta",
    [
        # Test that only the source sha256 and the version are rewritten
        (  # C1: Jinja version with no dashes, expect version and sha256 set
            '{% set version = "1.0.5" %}\n'
            "source:\n"
            "  sha256: 1b71d398d73800db32b09785af0e7\n",
            '{% set version = "1.0.6" %}\n'
            "source:\n"
            "  sha256: 123456789abcdef0123456789\n",
        ),
        (  # C2: sha256 held in a Jinja variable, expect the variable set
            '{% set version = "1.0.5" %}\n'
            '{% set sha256 = "1b71d398d73800db32b09785af0e7" %}\n'
            "source:\n"
            "  sha256: {{ sha256 }}\n",
            '{% set version = "1.0.6" %}\n'
            '{% set sha256 = "123456789abcdef0123456789" %}\n'
            "source:\n"
            "  sha256: {{ sha256 }}\n",
        ),
        (  # C3: sha256 outside source, expect only the source one rewritten
            '{% set version = "1.0.5" %}\n'
            "source:\n"
            "  sha256: 1b71d398d73800db32b09785af0e7\n"
            "test:\n"
            "  sha256: 0000000000000000000000000\n",
            '{% set version = "1.0.6" %}\n'
            "source:\n"
            "  sha256: 123456789abcdef0123456789\n"
            "test:\n"
            "  sha256: 0000000000000000000000000\n",
        ),
    ],
)
def test_update_meta_yaml(original_meta, expected_updated_meta, tmp_path):
    meta_file = tmp_path / "meta.yaml"
    meta_file.write_text(original_meta)
    _update_meta_yaml(str(meta_file), "1.0.6", "123456789abcdef0123456789")
    assert meta_file.read_text() == expected_updated_meta


@pytest.mark.parametrize(
    "original_meta, expected_error_msg",
    [
        # Test that an ambiguous recipe is refused instead of corrupted
        (  # C1: No version line, expect the recipe reported as unsupported
            "source:\n  sha256: 1b71d398d73800db32b09785af0e7\n",
            "No '{% set version = ... %}' line was found",
        ),
        (  # C2: Two sources, expect the count reported so nothing is guessed
            '{% set version = "1.0.5" %}\n'
            "source:\n"
            "  - url: https://example.com/a.tar.gz\n"
            "    sha256: 1b71d398d73800db32b09785af0e7\n"
            "  - url: https://example.com/b.tar.gz\n"
            "    sha256: 0000000000000000000000000\n",
            "found 2",
        ),
        (  # C3: No sha256 at all, expect the count reported as zero
            '{% set version = "1.0.5" %}\npackage:\n  name: example\n',
            "found 0",
        ),
    ],
)
def test_update_meta_yaml_bad_recipe(
    original_meta, expected_error_msg, tmp_path
):
    meta_file = tmp_path / "meta.yaml"
    meta_file.write_text(original_meta)
    with pytest.raises(ValueError, match=re.escape(expected_error_msg)):
        _update_meta_yaml(str(meta_file), "1.0.6", "123456789abcdef0123456789")
    # The recipe is left untouched when it cannot be updated safely
    assert meta_file.read_text() == original_meta


@pytest.mark.parametrize(
    "url, expected_slug",
    [
        # Test that equivalent GitHub remote URLs compare equal
        # C1: HTTPS URL with the .git suffix
        (
            "https://github.com/conda-forge/my-package-feedstock.git",
            "conda-forge/my-package-feedstock",
        ),
        # C2: HTTPS URL without the .git suffix
        (
            "https://github.com/conda-forge/my-package-feedstock",
            "conda-forge/my-package-feedstock",
        ),
        # C3: SSH URL, expect the same slug as the HTTPS forms
        (
            "git@github.com:conda-forge/my-package-feedstock.git",
            "conda-forge/my-package-feedstock",
        ),
        # C4: Mixed case and a trailing slash, expect lowercase and no slash
        (
            "https://github.com/Conda-Forge/My-Package-Feedstock/",
            "conda-forge/my-package-feedstock",
        ),
    ],
)
def test_get_repo_slug(url, expected_slug):
    assert _get_repo_slug(url) == expected_slug


def test_list_feedstock(tmp_path):
    # Test that only feedstock directories are listed, sorted by name
    for dir_name in ("b-feedstock", "a-feedstock", "not-a-package"):
        (tmp_path / dir_name).mkdir()
    (tmp_path / "c-feedstock").write_text("a file, not a directory")
    assert _list_feedstock(tmp_path) == ["a-feedstock", "b-feedstock"]


@pytest.mark.parametrize(
    "is_dir_created, expected_error_msg",
    [
        # Test that an unusable feedstock directory is reported clearly
        # C1: Directory holds no feedstocks, expect the user told to clone
        (True, "No feedstocks found in"),
        # C2: Directory is missing, expect the user pointed at ~/.skpkgrc
        (False, "was not found"),
    ],
)
def test_list_feedstock_bad_directory(
    is_dir_created, expected_error_msg, tmp_path
):
    feedstock_path = tmp_path / "feedstocks"
    if is_dir_created:
        feedstock_path.mkdir()
    with pytest.raises(ValueError, match=expected_error_msg):
        _list_feedstock(feedstock_path)


@pytest.mark.parametrize(
    "package_name, expected_submodules",
    [
        ("my_project", ["my_project"]),
        ("my_project.submodule", ["my_project", "submodule"]),
        ("diffpy.my_project.submodule", ["diffpy", "my_project", "submodule"]),
    ],
)
def test_resolve_namespace_package_name(package_name, expected_submodules):
    spec = importlib.util.spec_from_file_location(
        "post_gen_project",
        Path(__file__).parents[1] / "hooks" / "post_gen_project.py",
    )
    post_gen_project = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(post_gen_project)

    actual_submodules = post_gen_project.resolve_namespace_package_name(
        package_name
    )
    assert actual_submodules == expected_submodules


def test_update_package(user_filesystem, mocker):
    # C1: Run update_package to copy files from old-package-dir to
    #    new-package-dir and remove example files.
    #    Expect files in the old-package-dir to be copied to the
    #    new-package-dir, and example files are removed.
    spec = importlib.util.spec_from_file_location(
        "post_gen_project",
        Path(__file__).parents[1] / "hooks" / "post_gen_project.py",
    )
    post_gen_project = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(post_gen_project)
    # set up directory structure
    old_package_dir = user_filesystem / "my_package"
    new_package_dir = old_package_dir / "my_package"
    package_dir_name = "my_package"
    github_repo_name = "my_package"
    example_files = [
        f"docs/source/api/{package_dir_name}.example_package.rst",
        "docs/source/getting-started.rst",
        "tests/test_functions.py",
        "docs/source/img/scikit-package-logo-text.png",
        "docs/source/snippets/example-table.rst",
        f"src/{package_dir_name}/functions.py",
    ]
    example_file_paths = []
    for f in example_files:
        file_path = new_package_dir / f
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("example content")
        example_file_paths.append(file_path)
    old_package_file = old_package_dir / "README.md"
    old_package_file.write_text("# Old Package")
    # run update_package
    mocker.patch("pathlib.Path.cwd", return_value=new_package_dir)
    post_gen_project.update_package(
        github_repo_name=github_repo_name, package_dir_name=package_dir_name
    )
    # check that old package file is copied
    new_package_file = new_package_dir / "README.md"
    expected_content = "# Old Package"
    actual_content = new_package_file.read_text()
    assert actual_content == expected_content
    # check that example files are removed
    for file_path in example_file_paths:
        assert not file_path.exists()
