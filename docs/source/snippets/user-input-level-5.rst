  .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Prompt
        - Description and example
      * - authors
        - The name(s) and email address(es) of the project author(s). Please separate people with semicolons.
          e.g., Simon Billinge <sbillinge@ucsb.edu>; Sangjoon Lee <bobleesj@stanford.edu>
      * - maintainers
        - The name(s) and email address(es) of the project maintainer(s), using the same format as authors. Defaults to the authors. Both roles are listed in ``AUTHORS.rst``.
          e.g., Simon Billinge <sbillinge@ucsb.edu>; Yuchen Xiao <yxiao@columbia.edu>
      * - maintainer_github_usernames
        - The single GitHub username authorized to publish releases, even if the project has multiple maintainers.
          e.g., sbillinge
      * - contributors
        - Individuals or groups contributing to the project.
          e.g., Sangjoon Lee, Simon Billinge, Billinge Group members
      * - license_holders
        - The license holders listed in ``LICENSE.rst``.
          e.g., diffpy.utils contributors
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
        - The name of the package directory under ``src``. This name will be used in
          when importing modules from this package.
          Use ``name_with_underscores`` e.g., my_package
      * - project_short_description
        - A brief description of the project, shown in ``pyproject.toml``.
          e.g., A Python package standard for scientific code
      * - project_keywords
        - A list of keywords included in ``pyproject.toml``.
          e.g., PDF, diffraction, neutron, x-ray
      * - min_python_version
        - The minimum supported Python version.
          e.g. |PYTHON_MIN_VERSION|.  Current practice (`SPEC 0 specification <https://scientific-python.org/specs/spec-0000/>`_) is to drop support
          for Python versions that were released more than 72 months ago.
      * - max_python_version
        - The maximum supported Python version
          e.g. |PYTHON_MAX_VERSION|.  Ideally, the current latest version.
      * - needs_c_code_compiled
        - Specifies whether C code compilation is required.
          For pure Python packages, the default value is ``No``.
      * - has_gui_tests
        - Specifies whether GUI tests are included.
          For most packages, the default value is ``No`` but will be
          yes if your app has a gui and there are tests that run the GUI.
