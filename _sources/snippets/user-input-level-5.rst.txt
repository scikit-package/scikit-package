  .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Field
        - Description and example
      * - maintainer_name
        - The name of the project maintainer.
          e.g., Simon Billinge
      * - maintainer_email
        - The maintainer's email address.
          e.g., sbillinge@columbia.edu
      * - maintainer_github_username
        - The maintainer's GitHub username.
          e.g., sbillinge
      * - contributors
        - Individuals or groups contributing to the project.
          e.g., Sangjoon Lee, Simon Billinge, Billinge Group members
      * - license_holders
        - The license holders listed in ``LICENSE.rst``.
          e.g., The Trustees of Columbia University in the City of New York
      * - project_name
        - The name displayed in the ``README.rst`` and documentation.
          Use ``name-with-hyphens`` e.g., ``my-package``.
          To support namespace imports, see :ref:`FAQ <faq-project-setup-namespace>`
      * - github_username_or_orgname
        - The GitHub username or organization name.
          e.g., sbillinge or billingegroup
      * - github_repo_name
        - The GitHub repository name.
          Use ``name-with-hyphens`` e.g., my-package
      * - conda_pypi_package_dist_name
        - The name used for publishing to PyPI and conda-forge.
          Use ``name-with-hyphens`` e.g., my-package
      * - package_dir_name
        - The name of the package directory under ``src``.
          Use ``name_with_underscores`` e.g., my_package
      * - project_short_description
        - A brief description of the project, shown in ``pyproject.toml``.
          e.g., A Python package standard for scientific code
      * - project_keywords
        - A list of keywords included in ``pyproject.toml``.
          e.g., PDF, diffraction, neutron, x-ray
      * - min_python_version
        - The minimum supported Python version.
          e.g. |PYTHON_MIN_VERSION|
      * - max_python_version
        - The maximum supported Python version
          e.g. |PYTHON_MAX_VERSION|
      * - needs_c_code_compiled
        - Specifies whether C code compilation is required.
          For pure Python packages, the default value is ``No``.
      * - has_gui_tests
        - Specifies whether GUI tests are included.
          For most packages, the default value is ``No``.
