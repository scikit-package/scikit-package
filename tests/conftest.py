import json
from pathlib import Path

import pytest
import yaml

files_in_old_project = {
    ".git/COMMIT_EDITMSG": """
skpkg: last commit message in skpkg-package
""",
    "docs/source/tutorial.rst": """
The tutorial for skpkg-package.
""",
    "README.rst": """
|Icon| |title|_
===============

.. |title| replace:: title of README.rst in skpkg-package
""",
    "docs/source/index.rst": """
#######
|title|
#######

.. |title| replace:: title of skpkg-package documentation
""",
}
files_in_new_project = {
    ".git/COMMIT_EDITMSG": """
The file already exists in the new project
skpkg: last commit message in skpkg-package
""",
    "docs/source/tutorial.rst": """
The file already exists in the new project
The tutorial for skpkg-package.
""",
}


@pytest.fixture
def user_filesystem(tmp_path):
    base_dir = Path(tmp_path)
    home_dir = base_dir / "home_dir"
    home_dir.mkdir(parents=True, exist_ok=True)
    cwd_dir = base_dir / "cwd_dir"
    cwd_dir.mkdir(parents=True, exist_ok=True)

    home_config_data = {"username": "home_username", "email": "home@email.com"}
    with open(home_dir / "diffpyconfig.json", "w") as f:
        json.dump(home_config_data, f)

    old_package_dir = base_dir / "package-dir"
    for file_name, file_content in files_in_old_project.items():
        file_path = old_package_dir / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(file_content)
    empty_source_dir = base_dir / "empty-source-dir"
    empty_source_dir.mkdir()
    target_dir_inside_old_package_dir = (
        old_package_dir / "target-dir-inside-package-dir"
    )
    for file_name, file_content in files_in_new_project.items():
        file_path = target_dir_inside_old_package_dir / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(file_content)
    target_dir = base_dir / "target-dir"
    for file_name, file_content in files_in_new_project.items():
        file_path = target_dir / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(file_content)

    repo_info_dir_json = tmp_path / "repo_info_dir_json"
    repo_info_dir_yaml = tmp_path / "repo_info_dir_yaml"
    repo_info_dir_json_incomplete = tmp_path / "repo_info_dir_json_incomplete"
    skpkg_file = home_dir / ".skpkgrc"
    empty_skpkg_file = tmp_path / "another_home_dir" / ".skpkgrc"
    another_repo_info_dir_json = tmp_path / "another_repo_info_dir_json"
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
    another_groups_dict = {
        "small_group": ["repo1", "repo2"],
        "large_group": ["repo101", "repo102"],
    }
    another_repos_dict = {
        "repo1": "https://github.com/user/repo1",
        "repo2": "https://github.com/user/repo2",
        "repo101": "https://github.com/user/repo101",
        "repo102": "https://github.com/user/repo102",
    }
    repo_info_dir_json.mkdir()
    with (
        open(repo_info_dir_json / "groups.json", "w") as groups_file,
        open(repo_info_dir_json / "repos.json", "w") as repos_file,
    ):
        json.dump(groups_dict, groups_file)
        json.dump(repos_dict, repos_file)
    repo_info_dir_yaml.mkdir()
    with (
        open(repo_info_dir_yaml / "groups.yaml", "w") as groups_file,
        open(repo_info_dir_yaml / "repos.yaml", "w") as repos_file,
    ):
        yaml.dump(groups_dict, groups_file)
        yaml.dump(repos_dict, repos_file)
    repos_dict.pop("repo1")
    repo_info_dir_json_incomplete.mkdir()
    with (
        open(
            repo_info_dir_json_incomplete / "groups.json", "w"
        ) as groups_file,
        open(repo_info_dir_json_incomplete / "repos.json", "w") as repos_file,
    ):
        json.dump(groups_dict, groups_file)
        json.dump(repos_dict, repos_file)
    skpkg_file.write_text(
        json.dumps({"url_to_repo_info": str(another_repo_info_dir_json)})
    )
    empty_skpkg_file.parent.mkdir(parents=True, exist_ok=True)
    empty_skpkg_file.write_text(json.dumps({"some_key": "some_value"}))
    another_repo_info_dir_json.mkdir()
    with (
        open(another_repo_info_dir_json / "groups.json", "w") as groups_file,
        open(another_repo_info_dir_json / "repos.json", "w") as repos_file,
    ):
        json.dump(another_groups_dict, groups_file)
        json.dump(another_repos_dict, repos_file)

    yield tmp_path
