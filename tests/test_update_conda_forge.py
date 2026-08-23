import importlib
from pathlib import Path

import pytest

from scikit_package.cli.update.conda_forge import _update_meta_yaml


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
