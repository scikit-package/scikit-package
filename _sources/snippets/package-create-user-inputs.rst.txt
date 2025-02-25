#. Type ``package create`` inside the project directory.

#. Answer the questions as follows.

``proj`` stands for "project" and ``gh`` for "GitHub".

:proj_owner_name: e.g., ``Simon J. L. Billinge``.

:proj_owner_email: e.g., ``sbillinge@columbia.edu``.

:proj_owner_gh_username: e.g., ``sbillinge``.

:contributors: e.g., ``Billinge Group members and community contributors``.

:license_holders: e.g., ``The Trustees of Columbia University in the City of New York``.

:project_name: e.g., ``my-package``. For a namespace package, use e.g., ``diffpy.my-package``.

:github_org: The GitHub organization name or owner's GitHub username. e.g., ``diffpy`` or ``sbillinge``.

:github_repo_name: e.g., ``my-package``. The repository name of the project displayed on GitHub.

:package_dist_name: The name in the package distribution in PyPI and conda-forge. If your package name contains ``_``, replace it with ``-``. e.g., ``my-package``. For a namespace package, use e.g., ``diffpy.my-package``.

:package_dir_name: The name of the package directory. e.g., ``src/my_package``. Unlike ``project_name``, it must be lowercase so that it can be imported as ``import my_package``.

:proj_short_description: e.g., ``Python package for doing science.``

:keywords: Each word is separated by a comma and a space. e.g., ``pdf, diffraction, neutron, x-ray``. The keywords may be found in ``pyproject.toml`` or ``setup.py``.

:min_python_version: The minimum Python version for package distribution.

:max_python_version: The maximum Python version for package distribution.

:needs_c_code_compiled: Whether the package requires C/C++ code that requires building the package. For pure Python packages, type ``1`` to select ``No``.

:has_gui_tests: Whether the package runs headless testing in GitHub CI. If your package does not contain a GUI, type ``1`` to select ``No``.

#. Type ``ls`` to see the project directory.

#. Type ``cd <package_dir_name>`` to change the directory to the re-packaged directory.
