=============
Release notes
=============

.. current developments

0.3.1
=====

**Changed:**

* Use PyCQA/docformatter to format python docstring.
* Updated pre-commit hook versions in pre-commit-config file.

**Fixed**:

* Fixed running single docs-on-dispatch workflow on Github Action
* Fix post_gen hook: fall back to template default for unknown workflow_input keys


0.3.0
=====

**Added:**

* Enable configuring Python versions either in pyproject.toml or GitHub workflow .yml files.
* Support Python 3.14.
* Add ``package add deprecation`` to print deprecation docstrings.
* Add documentation for how to deprecate functions.
* Added documentation for a local installation with the package update and package create commands.
* Add package broadcast <issue-url> to broadcast a issue to multiple GitHub repositories.
* Run package update on scikit-package.
* Added step in release checklist to run manually dispatch matrix tests.
* Support setting multiple authors and maintainers.

**Changed:**

* Add `.placeholder` for `img` and `snippets` to replace example files when user run `package update`
* Changed ``package add news`` by removing ``-m`` flag. User now specifies message directly after specified flag with no ``-m`` necessary.

**Fixed:**

* use ``news`` from the repo in the tests since ``news`` is added in the source list.
* update m2r dependence to m2r2 everywhere
* Get the correct scikit-package version

**Removed:**

* Remove Python 3.11.


0.2.1
=====

**Fixed:**

* Remove the directory ``news/`` dependency to pass the tests.
* handle package names containing dashes during ``package update``.


0.2.0
=====

**Added:**

* Let ``package create <subcommand> -h`` display help text.
* Add the ``package update`` command to update existing ``sckit-package`` standard packages.
* Include package build api-doc instruction for namespace import.
* Use the latest release tag for all entry points of running cookiecutter.
* Add ``app.py`` file for basic CLI and add ``--version`` command for ``scikit-package``.
* Add tutorial for ``scikit-package-manuscript``.
* Add an instruction how to run extra custom CLI commands in test-on-pr and matrix CI.
* Add instructions for creating a news item by running ``package add news --<news-type> -m "<message>"`` in the documentation.
* Add ``docformatter`` configuration in ``pyproject.toml``.
* Add unit tests for updating meta.yaml for package update conda-forge and news item for package add news.
* Implement ``package add news -a -m "<message>"`` and ``package add no news -m "<message>"`` to streamline news item creation process
* Implement ``package build api-doc`` CLI to generate API .rst files for namespace support packages.
* Check the package is available on PyPI right after running package create conda-forge.
* Allow user to reuse the input in the prompts through project-level config file.
* Include introductory code snippets under the Getting Started page for first-time users.
* Correct typos and mistakes in migration portion of documentation.
* Implement ``package update feedstock`` to streamline making a conda-forge feedstock version update PR after PyPI release.
* Add instruction on how to use package update conda-forge in the conda-forge release guide
* Add tutorial in docs for how to call workflow files that don't upload to Codecov.
* Provide a better help description for ``package add news`` command.

**Fixed:**

* Fix ``pre-commit`` errors in PR template, init file generator, and ``test_functions.py``
* Use plural names from /doc to /docs and requirements/test.txt to requirements/tests.txt.
* Use simpler assertions in ``test_copy_all_files_bad``.

**Removed:**

* Remove ``$`` from codeblock in documentation.


0.1.0
=====

**Added:**

* Describe the difference between public and private functions in level 2 of the documentation.
* Provide instructions on how to ensure CHANGELOG.rst can be modified during release by bypassing rulesets if there are any.
* Provide an instruction when not to follow the file/folder naming convention for configuration files.
* Include a demo GIF file in the Sphinx documentation.
* Add note to instruct users to keep functions as modular as possible.
* Add 5 entry points (Lv1-3, Lv4, Lv5, Lv4-5, legacy to Lv5) in the tutorials section and the overview page.
* Add entry point of ``package create manuscript`` to create a manuscript template.
* Add ``package create conda-forge`` command to create a conda-forge recipe meta.yml file.
* Add instruction when to use hyphens or underscores for file and folder names under FAQ.
* Start implementing guilabel in Sphinx for clickable items in tutorials.
* Add tutorial for migrating Level 4 to Level 5 of sharing code.
* Add reasons we have adopted README.rst in Level 5 under FAQ section.
* Add Billinge group coding standards and workflows as a standalone section in the official ``scikit-package`` documentation.
* Add PR template to save maintainer's time and to help contributors generate and update public facing documentations.
* Add .readthedocs.yaml under the template folder to allow preview documentation on each PR.
* Add instructions on how to use alias shortcut for creating news file in Level 5.
* Implement package create workspace, package create system, and package create public CLI commands.
* Add descriptions on conda-forge, conda, and installers like miniconda, miniforge in the FAQ section.
* Include an example section in the official documentation.
* Allow preview rendered documentation in each pull request.
* Provide a starting template for Sphinx on how to reuse .rst file, attach images, and write code snippets in the documentation.
* Add a figure on pre-commit local and remote setup across Level 3 to 5 under FAQ.
* Support for copying code-blocks in documentation using sphinx_copybutton extension.
* Define clear roles for the owner and maintainer. The maintainer has merge and release rights, while the owner oversees the project, similar to a Principal Investigator (PI) in a research group.
* Add an example piece of code under the src directory to show how to develop new lines of code.
* Add section dividers in the nav of the ``scikit-package`` documentation into getting started, tutorials, release guides, programming guides, examples, support, and reference.
* Add a guide to use ``.rst`` backquotes for writing news items.
* Add instructions on how to render API ``.rst`` files without forking for standard and include a keyboard shortcut for using auto_api.py to generate API ``.rst`` files for package with namespace.
* Add descriptions for each workflow in Level 5 in a PR.
* Add an explicit instruction to configure conda-forge channel in Level 4, 5 tutorial instructions.
* Add instruction on how to avoid pre-commit auto-fix stash problem in the FAQ section.
* Add instruction on how to migrate ``.md`` to ``.rst`` file using a tool during Level 4 to 5 migration.
* Indicate the correction software version will be available in documentation built by readthedoc in each PR.
* Add "Edit on GitHub" link for each page in the documentation.
* Add docstrings to the dot_product function used for the demo code.
* Add how to solve CI error encountered with news GitHub CI under FAQ.
* Add logo to documentation header.
* Add instructions to use ``vulture`` in Level 5 and before PyPI release.
* Add a FAQ section on which workflow files to update when there is a new stable Python version.
* Add ``$`` for shell script commands in the documentation.
* Add instrunctions on how to setup write permission in GitHub workflows at the org and repository level.
* Add instructions on how to set logo and favicon in the documentation.
* Add step-by-step guides for Level 1 through Level 4 of sharing code.
* allow user to set default configs from `.skpkgrc`.
* allow user to change configs path by system variable `SKPKG_CONFIG_FILE`
* Add ``_build`` to ``.gitignore`` to prevent accidental commit of docs when using ``sphinx-reload``.

**Changed:**

* Instruct user to install API .rst file generation package from conda-forge instead of PyPI.
* Update QR code linking to the scikit-package documentation after migrating from Billingegroup.
* Provide step-by-step command-line instructions for Level 1 through 3 tutorials with recommended setup using Git for Windows and bash configuration.
* Modify Development Status from 5 to 3 in ``pyproject.toml``.
* Adopt Semantic Versioning 2.0.0 for pre-release GitHub tag name.
* Change cookiecuter user input value from ``github_org`` to ``github_username_or_orgname``.
* Transfer repository from billingegroup org to ``scikit-package`` org.
* Change ``github_admin_username`` to ``maintainer_github_username`` in release workflow to be compatible with skpkg.
* Change ``proj_owner`` to ``maintainer`` in Level 5 user inputs in cookiecutter to reflect that any developer including the project owner can help with package maintenance.

**Fixed:**

* Add ``make`` to ``requirements/docs.txt``.
* Refactor ``package create`` subcommands to easily add more commands under ``app.py``.
* Use the latest user prompts from ``package create conda-forge`` for ``meta.yml`` creation.
* Lowercase package directory name under src directory for namespace package.
* Update ``GITHUB_ADMIN_USERNAME`` to ``MAINTAINER_GITHUB_USERNAME`` in ``post_gen_hook.py`` to dynamically generate GitHub workflow files.
* Fixed the problem of a directory folder not being initialized with underscore.
* Remove the import of extend_path from pkgutil in ``diffpy/__init__.py`` in ``post_gen_hook.py`` when creating a new project with with the project name of ``<org-name>.<project-name>``.
* Remove ``requirements/README.txt`` containing instructions for listing dependencies for the package. The instruction is already provided in the official documentation.

**Removed:**

* Prevent running additional tests-on-PR CI when a PR is merged.
* Remove hard-coded ``diffpy`` in README.
* Remove environment.yml in the cookiecutter and skpkg repos since the centralized scripts no longer require it as the conda-forge channel is set in those scripts by default.


0.0.3
=====

**Added:**

* Added new logo
* Add a one-liner in README and index that the package is built and maintained using ``scikit-package``.
* Add logo for Github social preview.


0.0.2
=====

**Changed:**

* Provide separate documentation instructions for starting a new project vs. migrating an existing package.


0.0.1
=====

**Added:**

* Add full description of ``scikit-package`` in ``pyproject.toml``.
* Add motivating statements under the Statement of need section in ``index.rst``.
* Add ``package create`` and ``package update`` commands once ``scikit-package`` is installed.
* Add instructions on pre-commit GitHub setup, how to test package and render doc locally
* Add FAQ descriptions on Github workflow, namespace package setup, deploy docs via GitHub Actions
* Add extra metadata of email, name, username, license holder, etc. collected to dynamically populate rendered cookiecuttered files.
* Add conda-forge feedstock creation and maintenance guide.
* Add instructions for Codecov setup in documentation.
* Add FAQ section to the documentation on how to customize the template and design decisions for the current setup.
* Add demo .gif file used in README.rst in generating a package and building documentation with ``scikit-package``.
* Add ``Getting started`` page in documentation.
* Add FAQ section on why both ``pip.txt```` and ``conda.txt`` added.
* Add FAQ section on how version is set and retrieved dynamically.
* Support Billinge group's reusesable workflow by adding requirement files and ``environment.yml``.
* Add Sphinx documentation for ``scikit-package``.
* Add documentation for Python package release with GitHub Actions.
* Use field-list feature in Sphinx to better manage the user inputs in How to cookiecut package section
* Add automatic linting of .md, .yml, .rst files via prettier hook in ``pre-commit``.
* Add automatic docstring linting with PEP 257 compliance with ``docformatter`` in ``pre-commit``.
* Configure ``PYTHON_MAX_VERSION`` and ``PYTHON_MIN_VERSION`` in ``docs/source/conf.py`` to increase maintainability throughout the documentation.

**Changed:**

* Rename repositroy and package name to ``scikit-package``.
* Import ``package_dir_name```` in the ``__init__.py`` instead of ``conda_pypi_package_dist_name`` to ensure package import is lowercased.
* Change default line-length to 79 characters in ``black``, ``flake``, and ``isort`` configuration files for PEP8 compatibility.
* Change question and default answer format on user prompt on C extension and headless GUI with improved wording.
* Standarlize the current repository based on ``scikit-package`` structure.

**Fixed:**

* Update corresponding email to sbillinge@ucsb.edu.
