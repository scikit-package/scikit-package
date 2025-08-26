.. index:: frequently-asked-questions

.. _frequently-asked-questions:

================================
Frequently asked questions (FAQ)
================================

Here, you will learn how to customize the ``scikit-package`` template for your own project, such as setting the line-width and including/excluding files for PyPI distribution. We also provide design decisions for the current setup of the ``scikit-package`` template.

.. _faq-pre-commit:

Pre-commit
----------

``Pre-commit`` attempts to automatically fix code style issues. The following questions are used to customize the ``pre-commit`` configuration for your project's needs.

.. _faq-pre-commit-levels:

How is pre-commit used in each Level?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is a recommended setup and hooks for ``pre-commit`` for each level:

.. list-table::
  :header-rows: 1

  * - Level
    - Name
    - Recommended setup
    - Hooks used
  * - 3
    - ``workspace``
    - Run ``pre-commit run --all-files`` locally.
    - Automatic linting with ``black``, ``prettier``, ``docformatter``
  * - 4
    - ``system``
    - Use ``pre-commit install`` locally, ``pre-commit CI`` in GitHub
    - Level 3 hooks, PEP 8 check with ``flake8``, default hooks (merge conflicts, end-of-file-fixer, etc.)
  * - 5
    - ``public``
    - Same as Level 4
    - Level 4 hooks, no commits to ``main``, spell checker with ``codespell``,


How do I modify line-width limits?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following files need to be modified:

#. In ``.isort.cfg``, modify ``line_length``.
#. In ``.flake8``, modify ``max-line-length``.
#. In ``pyproject.toml``, modify ``line-length`` under ``[tool.black]``.

.. seealso::

  As recommended by PEP 8, comments and docstrings should be wrapped at 72 characters, as defined under ``[tool.docformatter]`` in ``pyproject.toml``.

How do I skip a specific file for ``flake8`` and ``black``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To skip files checked by ``flake8``, include the file path in ``.flake8`` under the ``exclude`` section.

To prevent ``black`` from formatting, include the file path in ``pyproject.toml`` under the ``[tool.black]`` section.

How do I suppress the ``flake8`` error?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ad ``# noqa: <error-code>`` at the end of the line. For example, ``import numpy as np # noqa: E000``.

.. _faq-pre-commit-error:

How do I fix conflicted hook auto-fix errors?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may encounter the following error message when you run ``git commit -m <your-commit-message>``: ::

  Stashed changes conflicted with hook auto-fixes...

To solve this problem, run ``git add <file>`` on the files modified by ``pre-commit``. Then, re-enter same commit message above using ``git commit -m <your-commit-message>``. Why do we need to run ``git add`` again? The files that are linted by ``pre-commit`` are not staged to the local Git database. So, we stage them manually again with ``git add``.

.. _faq-codespell-ignore:

How do I ignore words/lines/files in automatic spelling checks in pre-commit?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/codespell-ignore.rst

Project setup
-------------

.. _faq-project-setup-namespace:

I read ``scikit-package`` allows namespace support for importing packages. What is it, and how do I set it up?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A research group often maintains multiple software packages under a single GitHub organization.
For the purposes of branding and also differentiating packages with similar names, it can sometimes be beneficial for the organization or research group name (or some other branding name) to appear in the package name itself.

Here is an example. Consider the package called ``diffpy.pdffit2``. The package starts with an organization identifier of ``diffpy``, and the package name is ``pdffit2``. There is a separate GitHub repository for this package (https://github.com/diffpy/diffpy.pdffit2) while it is developed under the DiffPy organization (https://github.com/diffpy). The user can import the package as ``import diffpy.pdffit2 as pdffit2`` in any Python script.

.. note::

  This namespace feature is only available in Level 5, ``public``. In programming, a "namespace" refers to a unique identifier that can hold many classes, functions, and variable names. Here we extend the concept that the top level namespace holds multiple packages.

What is the difference in folder structure compared to a standard package?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

For a standard package, the folder structure is as follows:

.. code-block:: text

  ├── src
  │   ├── <package_name>
  │   │   ├── __init__.py
  │   │   ├── file_one.py
  │   │   ├── file_two.py

For a package to be imported using ``import <namespace_name>.<package_name>``, the folder structure is as follows:

.. code-block:: text

  ├── src
  │   ├── <namespace_name>
  │   │   ├── __init__.py
  │   │   └── <package_name>
  │   │       ├── __init__.py
  │   │       ├── file_one.py
  │   │       ├── file_two.py

How do I set it up with ``scikit-package``?
"""""""""""""""""""""""""""""""""""""""""""

Our ``scikit-package`` automatically handles this folder setup for you! When you run ``package create public``, simply enter ``project_name`` as, e.g., ``<namespace_name>.<package_name>``, like the default value provided. ``scikit-package`` adjusts the folder structure based on the presence of the ``.`` that separates the ``<namespace_name>`` and ``<package_name>``.

In Level 5, why do we adopt ``README.rst`` instead of ``README.md``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We adopt ``README.rst`` at Level 5 because reStructuredText (``.rst``) provides a more configurable format and control. One key advantage of ``.rst`` is its native support for advanced formatting, such as precise control over image size and layout: ::

  .. |Icon| image:: img/logos/scikit-package-logo-text.png
      :target: https://scikit-package.github.io/scikit-package
      :height: 150px

Achieving the same result in Markdown often requires raw HTML, which is less readable and may render inconsistently across platforms.

Switching to ``README.rst`` at Level 5 helps users appreciate the formatting power of ``.rst`` and serves as a stepping stone toward writing full documentation in ``.rst`` as part of the ``scikit-package`` documentation standard.

.. _faq-set-default-prompt-value:

How can I change the default values that appear in the prompt when creating projects in Level 3,4,5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can override the existing default values in the prompt by creating and editing a configuration file ``.skpkgrc`` in the user ``home`` directory. In ``bash`` your ``home`` directory is designated by ``~``.

Here are the steps you can follow to override the default values for Level 5 usage.

1. Go to ``home`` directory.

  .. code-block:: bash

    cd ~

2. Create ``.skpkgrc``.

  .. code-block:: bash

    touch .skpkgrc

3. Edit ``.skpkgrc``. Copy and paste the following snippets to ``.skpkgrc``.

  .. code-block:: json

    {
      "default_context":
        {
            "maintainer_name": "<local-default-maintainer-name>",
            "maintainer_email": "<local-default-maintainer-email>",
            "maintainer_github_username": "<local-default-maintainer-github-username>",
            "github_username_or_orgname": "<local-default-github-username-or-orgname>",
            "contributors": "<local-default-contributors-name>",
            "license_holders": "<local-default-license-holders-name>",
            "project_name": "<local-default-project-name>",
        }
    }

4. Replace words in angle brackets with values you prefer. These values will be your new default values when you run scikit-package on your local machine. In your ``.skpkgrc`` you may delete any rows that you do not want to modify from the package defaults.

.. seealso::

    Creating packages in Level 3, 4 and 5 requires different entries. When you create a package at a certain level, only the entries with matched names will be processed. So irrelevant entries have no effect and you can set all the level 3, 4 and 5 default values in ``.skpkgrc``.

How can I change the location of configuration file?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The scikit-package configuration file is located in ``~/.skpkgrc`` by default. You can use the environment variable ``SKPKG_CONFIG_FILE`` to change its location.

.. code-block:: bash

   export SKPKG_CONFIG_FILE=/path/to/config


Release
-------

.. _release_authority:

How can I change who is authorized to release a package?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In ``.github/workflows/build-wheel-release-upload.yml``, modify ``maintainer_github_username`` to the desired GitHub username. This username will be able to authorize the release by pushing the tag as instructed in :ref:`release-pypi-github`.

.. _faq-release-ci-failed:

Release CI failed. What should I do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pre-release:

- Did you encounter an error under the ``privilege-check`` section in the workflow? Ensure the user performing the release has the GitHub username specified in ``maintainer_github_username`` under ``.github/workflows/build-wheel-release-upload.yml``.
- Did you encounter an error related to ``PYPI``? Ensure you have ``PAT_TOKEN`` configured at the organization or repository level. Please read :ref:`pypi-token-setup`. Even if ``PYPI_TOKEN`` is already configured, ensure it is the latest token and has not been revoked or expired.

  .. note::

    As the next step, if you created and pushed ``*.*.*-rc.0``, you may simply bump and create a new version tag of ``*.*.*-rc.1`` and push it to the remote repository.

Release:

- Did you encounter an error related to ``fatal: could not read Username``? Ensure you have ``PAT_TOKEN`` configured at the organization or repository level. Please read :ref:`pat-token-setup`. Even if ``PAT_TOKEN`` is already configured, ensure it is the latest token and has not been revoked or expired.
- Did you encounter any error from ``Rulesets``? In your repository, visit :menuselection:`Settings --> Rules --> Rulesets`. Then click one or more of the rulesets. For each ruleset, under the :guilabel:`Bypass list`, click :guilabel:`Add bypass` and :guilabel:`Organization admin` to the ruleset. The GitHub workflow will use the ``PAT_TOKEN`` to bypass the ruleset.

  .. note::
    Here, we don't want to bump a new version. As the next step, delete the Git tag in the local by running ``git tag -d <tagname>`` and visit ``https://github.com/<org-or-username>/<package-name>/tags`` to delete it in the remote. Then, follow the same process for a full release by creating a new tag and pushing it to the remote.

How is the package version set and retrieved?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In ``pyproject.toml``, the ``setuptools-git-versioning`` tool is used to dynamically retrieve the version based on the latest tag in the repository. The latest tag is pushed during the release workflow. The dynamically parsed version is globally accessible, via ``<package-name>.__version__``.

How do I include/exclude files in PyPI release?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``MANIFEST.in`` file is used to control which files are included in the source distribution. Try running ``python -m build`` and see the content under the ``dist`` folder generated.

To include all files under a folder, use ``graft``:

.. code-block:: text

   graft src
   graft tests

To include specific file(s), use ``include``:

.. code-block:: text

   include AUTHORS.txt LICENSE*.txt README.rst

To exclude files globally, use ``globally-exclude``:

.. code-block:: text

   global-exclude *.py[cod]  # Exclude all .pyc, .pyo, and .pyd files.
   global-exclude .DS_Store  # Exclude Mac filesystem artifacts.
   global-exclude __pycache__  # Exclude Python cache directories.
   global-exclude .git*  # Exclude git files and directories.

Why have we decided to include test files in the PyPI source distribution?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We decided to include test files in the PyPI source distribution to facilitate unit testing with a newly built Conda package.

The conda-forge CI uses the source code distributed via PyPI to build a Conda package. After building the package, we want to run pytest to ensure all unit tests pass before release. Therefore, test files must be included in the source code. In contrast, no documentation is distributed with the package, as it is already accessible from the GitHub repository and does not serve a practical purpose in the distribution package itself.

Documentation
-------------

How can I preview the documentation in real-time?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/doc-local-build.rst

.. _faq-doc-api-standard:

How do I build API .rst files automatically for a standard Python package?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is how you can **automate** the process of generating API documentation for a standard Python package located in the ``docs/source/api`` folder.

.. note::

  Your package is considered a **standard package** if it is imported as ``import <package_name>`` instead of ``import <namespace_name>.<package_name>``.

#. Add ``sphinxcontrib-apidoc`` to the ``requirements/docs.txt`` file.

    .. code-block:: text

      sphinx
      sphinx_rtd_theme
      sphinx-copybutton
      sphinxcontrib-apidoc
      ...

#. Run ``conda install --file requirements/docs.txt`` to install the new dependency.

#. Replace the following code block in your ``docs/source/conf.py`` file from

    .. code-block:: python

        extensions = [
            "sphinx.ext.autodoc",
            "sphinx.ext.napoleon",
            "sphinx.ext.todo",
            "sphinx.ext.viewcode",
            "sphinx.ext.intersphinx",
            "sphinx_rtd_theme",
            "sphinx_copybutton",
            "m2r",
        ]

    to

    .. code-block:: python

        extensions = [
            "sphinxcontrib.apidoc",  # Add this extension to run sphinx-apidoc
            "sphinx.ext.napoleon",
            "sphinx.ext.todo",
            "sphinx.ext.viewcode",
            "sphinx.ext.intersphinx",
            "sphinx_rtd_theme",
            "sphinx_copybutton",
            "m2r",
        ]

        # Configure where to find the source code and write API .rst files
        apidoc_module_dir = '../../src/<package_dir_name>'
        apidoc_output_dir = 'api'
        apidoc_excluded_paths = ['tests']
        apidoc_separate_modules = True

#. Next to the ``apidoc_module_dir`` variable above, replace ``<package_dir_name>`` with the directory name under ``src``, e.g., ``my_package``.

#. Run ``sphinx-reload doc`` to build and host the documentation.

    Notice that the ``.rst`` files under ``docs/source/api`` are generated whenever the documentation is re-rendered.

#. Add the following block to your ``docs/source/index.rst`` file:

    .. code-block:: text

      .. toctree::
         :maxdepth: 2
         :caption: API Reference

          Package API <api/package_dir_name>

#. Now, you should see the :guilabel:`API Package` section in the left menu bar of the documentation. Click on it to see the API documentation.

#. Done! If you have any issues, please feel free to open an issue in the ``scikit-package`` GitHub repository.

.. _faq-doc-api-namespace:

How do I build API .rst files for a Python package with a namespace import?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install ``scikit-package`` if you haven't already:

    .. code-block:: bash

        conda install scikit-package

#. ``cd`` into your project directory:

    .. code-block:: bash

        cd <path-to-your-project>

#. Ensure you have the ``API`` section in ``docs/source/index.rst``:

    .. code-block:: text

      .. toctree::
         :maxdepth: 2
         :caption: API Reference

          Package API <api/package_dir_name>

#. Run the following CLI command to generate ``.rst`` files in ``docs/source/api``:

    .. code-block:: bash

        package build api-doc

#. Done!

.. _faq-doc-pr-preview:

How can I preview the documentation in each pull request?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/doc-pr-preview.rst

How do I re-deploy online documentation without another release?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Visit the following URL of your package: ``https://github.com/<org-name>/<package-name>/actions/workflows/publish-docs-on-release.yml`` i.e., https://github.com/diffpy/diffpy.utils/actions/workflows/publish-docs-on-release.yml.

Click ``Run workflow`` and select the ``main`` branch. Your online documentation will be updated with the latest changes without a new release.

.. _faq-doc-error-no-module-name:

How do I fix the "No module named" error when I render documentation?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(e.g., ``WARNING: autodoc: failed to import module 'tools' from module 'diffpy.pdfmorph'; the following exception was raised: No module named 'diffpy.utils'``), it can be resolved by adding ``autodoc_mock_imports = [<pkg>]`` to your ``conf.py`` right under imports. This file is located in ``/docs/source/conf.py``.

.. _faq-doc-favicon-logo:

How do I add a favicon and logo to the documentation?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In ``docs/source/conf.py``, add the following lines:

.. code-block:: python

  html_theme_options = {
    "navigation_with_keys": True,
    "logo_only": True,
  }

  html_favicon = "<path-to-favicon>"
  html_logo = "<path-to-logo>"

The clickable logo will be displayed above the menu bar on the left side of the page.

conda-forge
-----------

How do I add a new admin to the conda-forge feedstock?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please refer to the :ref:`Add a new admin <conda-forge-add-admin>` section.

How do I do pre-release for conda-forge?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please refer to the :ref:`How do I do pre-release? <conda-forge-pre-release>` section.

.. _faq-github-actions:

GitHub Actions
--------------

.. _faq-github-actions-python-versions:

In Level 5, How do I set different Python versions for GitHub CI?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python |PYTHON_MAX_VERSION| is the current default Python version in ``.github/workflows/tests-on-pr.yml`` and ``.github/workflows/publish-docs-on-release.yml``. Python |PYTHON_MIN_VERSION| to |PYTHON_MAX_VERSION| are used in ``.github/workflows/matrix-and-codecov-on-merge-to-main.yml``. To override the defaults, modify the three ``.yml`` files mentioned above in ``.github/workflows/`` as shown below:

1. Add ``python_version`` in ``.github/workflows/tests-on-pr.yml``:

.. code-block:: yaml

   jobs:
    tests-on-pr:
      uses: scikit-package/release-scripts/.github/workflows/_tests-on-pr.yml@v0
    with:
      project: package-name
      c_extension: false
      headless: false
      python_version: 3.12
    secrets:
      CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}

2. Add ``python_version`` in ``.github/workflows/_publish-docs-on-release.yml``:

.. code-block:: yaml

   jobs:
    docs:
      uses: scikit-package/release-scripts/.github/workflows/_tests-on-pr.yml@v0
    with:
      project: package-name
      c_extension: false
      headless: false
      python_version: 3.12

3. Add ``python_versions`` in ``.github/workflows/_matrix-and-codecov-on-merge-to-main.yml``:

.. code-block:: yaml

   jobs:
    matrix-coverage:
      uses: scikit-package/release-scripts/.github/workflows/_matrix-and-codecov-on-merge-to-main.yml@v0
    with:
      ...
      python_versions: "3.11, 3.12"

In Level 5, what are the workflows running in each pull request?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. The first workflow is called ``Tests on PR`` from ``.github/workflows/tests-on-pr.yml``. This workflow creates a new conda environment on Linux and installs the dependencies listed in the ``requirements`` folder using the ``conda-forge`` channel. The conda environment is configured to use the highest Python version specified when the project was initially created. It then runs the unit tests located in the ``tests`` folder, similar to how you would run them locally.

#. The second workflow uses ``pre-commit CI``. This workflow checks the incoming code in the PR using ``pre-commit`` hooks and automatically applies fixes when possible. If any fixes are made, an additional commit is created by the ``pre-commit`` app. However, some hooks, such as spell checkers, may still fail even after auto-fixes. In such cases, the CI fails. The user first needs to pull the additional commit made by the ``pre-commit CI``, fix the error manually, and then push a commit to the working branch.

#. The third workflow uses the ``Codecov`` app, which adds a comment to the PR summarizing the changes in code coverage as part of the ``.github/workflows/tests-on-pr.yml`` workflow. This workflow fails if no tests are provided for the new code or if the test coverage percentage decreases below the acceptable threshold. The threshold can be adjusted in the ``.codecov.yml`` file located in the project root directory. If you have a private repository and Codecov cannot be run, refer to :ref:`faq-private-repo-no-codecov`.

#. The fourth workflow checks for a news file in the PR using ``.github/workflows/check-news-item.yml``. If no news item is included for the proposed changes, this workflow fails and leaves a comment prompting the contributor to submit a new PR with the appropriate news file. Please refer to the best practices section on :ref:`news items <news-item-practice>`.

In Level 5, I see that another workflow is running once a PR is merged to ``main``. What is it?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The workflow ``.github/workflows/matrix-and-codecov-on-merge-to-main.yml`` is triggered. The goal is to ensure the latest code is tested not only on Linux but also across multiple operating systems and Python versions. This workflow runs tests on macOS (both Apple Silicon and Intel chips), Linux, and Windows and against three different Python versions, including the latest configured version. To modify the Python versions used in the workflows, refer to :ref:`faq-github-actions-python-versions`.

.. note:: These workflow files call scripts located at https://github.com/scikit-package/release-scripts, which are centrally managed by the ``scikit-package`` development team. This centralized approach ensures that individual packages do not need to be updated separately when adding support for new Python versions or operating systems.

I am encountering a 'build' is requesting 'pull-requests: write' error. How do I fix it?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-ci-permission.rst

What is the difference between ``pull_request`` and ``pull_request_target``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the current GitHub CI for checking a news item, ``pull_request_target`` is used instead of ``pull_request`` as shown below:

.. code-block:: yaml

   name: Check News Item

   on:
    pull_request_target:
      branches:
       - main

- ``pull_request``: This event configures the ``GITHUB_TOKEN`` with read-only permissions by default, especially when triggered by forks.
- ``pull_request_target``: This event grants the ``GITHUB_TOKEN`` write permissions, enabling it to perform actions that modify the repository, such as posting comments, updating pull request statuses, or merging code. The news CI creates a comment when an additional news ``.rst`` is not found under the ``news`` folder. Hence, ``pull_request_target`` is used.

Another key difference is that with ``pull_request_target``, the ``.yml`` file **must already be merged** in the base branch at the time the pull request is opened or updated. For more, please refer to `GitHub docs <https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#pull_request_target>`_.

.. _faq-github-actions-extra-cli-commands:

How can I add extra CLI commands in the GitHub workflow for running tests?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the GitHub workflow files for testing, you might want to add extra CLI commands **before** running ``pytest``. For example, you may want to install dependencies that are not available on ``conda-forge`` but are only available from PyPI to test your package.

To do so, you can enter the ``run:`` command under the ``with:`` section in the workflow file.

.. code-block:: yaml

  with:
    project: <package-name>
    run: |
      pip install <package-name>
      echo "Done installing <package-name>"
    ...

- In Level 5, the relevant workflow files are ``.github/workflows/matrix-and-codecov-on-merge-to-main.yml`` and ``.github/workflows/tests-on-pr.yml``.
- In Level 4, the relevant workflow file is ``.github/workflows/_tests-on-pr-no-codecov-no-headless.yml``.

Here we provide a bit more context on how the ``run:`` commands are used. The extra CLI commands are inserted into the reusable GitHub workflow under the ``Run extra user-defined CLI commands`` section of the reusable workflow file:

.. code-block:: yaml

      - name: Install ${{ inputs.project }} and requirements
        run: |
          conda install --file requirements/conda.txt
          conda install --file requirements/tests.txt
          if ${{ inputs.c_extension }}; then
            conda install --file requirements/build.txt
          fi
          python -m pip install . --no-deps

      - name: Run extra user-defined CLI commands
        run: |
          echo "${{ inputs.run }}" > user-commands.sh
          bash user-commands.sh

After this step, the reusable workflow then runs the ``pytest`` command. To see the full reusable workflow file, please visit https://github.com/scikit-package/release-scripts/blob/main/.github/workflows/_tests-on-pr.yml.

.. _faq-private-repo-no-codecov:

I have a private repo and don't have a Codecov paid plan.  Can I modify the CI workflows for this situation?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the workflows in ``tests-on-pr.yml`` and ``matrix-and-codecov-on-merge-to-main.yml`` will have a section that uploads the code coverage to Codecov, and CI will fail if unsuccessful. Codecov is available for free on public repositories but requires a paid plan to run on private repositories. In the latter case, if you would like to turn off Codecov, we offer an alternative CI workflow that runs the tests without it.

In addition to being able to customize additional commands to be run in the ``run:`` section (see :ref:`faq-github-actions-extra-cli-commands` above), you can also change the workflows that you want your repository to run. By default, ``scikit-package`` will run the ``tests-on-pr.yml`` and ``matrix-and-codecov-on-merge-to-main.yml`` workflows in the ``scikit-package/release-scripts`` repository. It is possible to override this default and run a different workflow for your CI if it is available in ``scikit-package/release-scripts``. For example, for the situation above we offer we offer ``tests-on-pr-no-codecov.yml`` and ``matrix-no-codecov-on-merge-to-main.yml`` which run the tests without Codecov.

To do so, you can modify the script that your workflow files are calling in the ``uses:`` section. Normally, you'd be calling the following in ``tests-on-pr.yml`` and ``matrix-and-codecov-on-merge-to-main.yml``, respectively.

.. code-block:: yaml

  uses: scikit-package/release-scripts/.github/workflows/_tests-on-pr.yml@v0

.. code-block:: yaml

  uses: scikit-package/release-scripts/.github/workflows/_matrix-and-codecov-on-merge-to-main.yml@v0

Instead, call the following in ``tests-on-pr.yml`` and ``matrix-and-codecov-on-merge-to-main.yml``, respectively.

.. code-block:: yaml

  uses: scikit-package/release-scripts/.github/workflows/_tests-on-pr-no-codecov.yml@v0

.. code-block:: yaml

  uses: scikit-package/release-scripts/.github/workflows/_matrix-no-codecov-on-merge-to-main.yml@v0

Don't forget to also delete the following section from your workflow files now that we are not uploading to Codecov in the workflows anymore.

.. code-block:: yaml

  secrets:
    CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}

Done! If you have a different situation that our current workflows have not accounted for, please feel free to contribute a new workflow file by making a PR.

.. _faq-dependency-management:

Dependency management
---------------------

.. _faq-dependency-files:

What are ``docs.txt``, ``tests.txt``, ``build.txt``, and ``conda.txt`` files under ``\requirements`` in Level 4 and Level 5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:pip.txt: list all PyPI packages required to install the package via `pip install <package-name>`.

:conda.txt: list all Conda packages required for running the package in GitHub CI. It should be typically identcal as the ``pip.txt`` file.

:tests.txt: packages required for the testing suite to ensure all tests pass.

:docs.txt: packages required for building the package documentation page.

:build.txt: list all conda packages required for building the package in GitHub CI, including those specified in the build section of meta.yaml (conda-recipe).

.. _faq-conda-ecosystem:

What is conda-forge?
^^^^^^^^^^^^^^^^^^^^

conda-forge is an open-source-software community-maintained channel on the conda/Anaconda package server. The structure of the Anaconda server is that packages are hosted and can be installed from user-maintained "channels", and the original vision was that different developers and organizations would put their own code on their own channels.

conda-forge is a community led effort to have a **single channel shared by everyone**. This also allows the community to develop package maintenance tools to help with the ecosystem such as auto tick bots that check when the latest version of a package is not present on conda-forge and alert the maintainers, and GitHub workflows to pre-build wheel files for all platforms and python versions. It also tries to resolve a dependency graph for a package to install the most recent version of every package that satisfies the requirements of all the sub-packages.

**We recommend making use of conda-forge and helping the community** by, where possible, installing from conda-forge and also making sure your package is available on conda-forge so others may install it from conda-forge.

Here is how you can add the conda-forge channel to your conda configuration and install the ``scikit-package`` package from it:

.. code-block:: bash

  conda config --add channels conda-forge
  conda install scikit-package

The first command adds the ``conda-forge`` channel to the conda configuration, allowing users to install packages from this channel. The second command installs the ``scikit-package`` package from the ``conda-forge`` channel. https://anaconda.org/conda-forge/scikit-package

What are Miniconda, Anaconda, and Miniforge?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While conda is an environment and package manager, it is itself a piece of software that must be installed locally. Several installers are available for this purpose:

- **Miniconda**: A minimal installer that includes only the necessary components to manage packages and environments. In ``scikit-package`` reusable GitHub workflows, we set up ``Miniconda`` as the default installer.

- **Anaconda**: A much larger installer that not only installs conda but also provides a pre-configured environment with Python and commonly used packages such as ``numpy``, ``pandas``, and ``Jupyter Notebook``. This comprehensive solution is often used for educational purposes, as students do not need to manually install additional packages.

- **Miniforge**: Another installer that includes conda, ``mamba``, and Python, with the ``conda-forge`` channel pre-configured. See the next section for more information on what ``mamba`` is.

Why do some people use mamba instead of conda?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recall that conda is a dependency manager that uses sophisticated algorithms to identify compatible software versions. As the number of dependencies increases, the solving process can become computationally expensive.

To address this, ``mamba`` was developed. ``mamba`` uses the same commands and configuration options as conda but features a faster dependency-solving algorithm written in C++. ``mamba`` is also compatible with existing conda environments (e.g., ``environment.yml``) and continues to rely on the conda ecosystem for package distribution, using channels like ``conda-forge``. When you install ``mamba`` using ``Miniforge``, the conda-forge channel is set as the default (and only) channel.

.. _faq-dependency-pip-conda-both-provided:

Why are both ``pip.txt`` and ``conda.txt`` provided?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Our preferred choice for installing the scikit-packaged package is as a Conda package, as outlined in the template ``README.rst`` file. With Conda, the end user can install all associated dependencies by running ``conda create --name new-env <package-name>``. Additionally, the environment is tested via conda-forge CI before the conda package is released, which helps ensure the package's compatibility with its dependencies. Hence, we list conda package dependencies in ``conda.txt``.

However, we also want to allow users to install the package via ``pip``. To support this, we provide a separate file for pip dependencies, ``pip.txt``. In most cases, the dependencies listed in ``conda.txt`` and ``pip.txt`` will be identical. However, there can be exceptions. For example, ``matplotlib-base`` is preferred for Conda installations, while ``matplotlib`` is used for pip installations.

.. _faq-github-workflow:

GitHub workflow
---------------

I am new to GitHub. Why do we use Git/GitHub?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GitHub allows multiple contributors to work on a software project simultaneously under an organization like ``Billingegroup`` or ``diffpy``. There are two primary needs. First, we want to ensure that any changes under this organization are reviewed by the organization's project maintainer. Second, we want to ensure we add new changes from the latest version of the code, particularly when working with multiple contributors across different time zones. Hence, we use GitHub to serve the needs with a specific workflow below. Please see below for an overview of the GitHub workflow.

.. _faq-github-workflow-overview:

What is the general the workflow?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting a new Python package in Level 4 and 5 requires a basic understanding of GitHub's workflow, we will provide you with a brief overview and how to set up your repository.

First, if you are working on a package from an organization like ``github.com/diffpy`` or ``github.com/Billingegroup``, you first copy the repository of the organization to your GitHub user account. This process is called ``forking``.

Then, you will download the forked repository in your GitHub account to your local machine. This process is called ``cloning``.

In the cloned repository on your local machine, you will make edits. You want to first add a description for the changes by "committing" with a message describing the changes. Then you will upload these changes to the ``forked`` repository in your account. This process of updating code from the local computer to the repository hosted by GitHub is called ``pushing``.

From the forked repository, you then want to upload changes to the repository under ``github.com/scikit-package/scikit-package``, for example. This process is done through a process called ``pull request``. The Project Owner reviews this pull request and merges it into the Billinge group's repository. If you are the contributor as well as the Project Owner, you would be the one who reviews your own code and merges your changes.

I have a general understanding of fork, clone, commit, push, and pull request. How do I set up my repository for packaging?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please be familiar with the terminology such as "fork", "clone", "push", and "pull request" explained above in :ref:`faq-github-workflow-overview`.

You may fork the repository using the "Fork" button on the top right corner of the repository page. This will copy the repository to your GitHub account. e.g., ``github.com/scikit-package/scikit-package`` to ``github.com/sbillinge/scikit-package``.

Then download the forked repository under your account to the local machine by cloning:

.. code-block:: bash

  git clone https://github.com/<username>/<package-name>

Now, you also want to link with the repository of the organization by adding the URL. Recall, we want to make changes from the latest state of the source code.

.. code-block:: bash

  git remote add upstream https://github.com/<org-name>/<package-name>

.. note::

   What is ``upstream``? The repository that you forked from, e.g. ``scikit-package/scikit-package`` is referred to as the ``upstream`` repository.

Verify that you have the ``upstream`` URL set up as the organization.

.. code-block:: bash

  git remote -v

Notice that you also have ``origin`` with an URL linking to your forked repository under your account. This is another GitHub jargon that refers to your forked repository.

.. note::

  What is ``remote``? The term ``remote`` is the opposite of ``local``. In other words, ``remote`` refers to the repository that is hosted by GitHub. e.g., ``github.com/scikit-package/scikit-package`` or ``github.com/sbillinge``.

.. _faq-github-terminology:

Do you have a general summary of each term used in the GitHub workflow?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:fork: The process of copying a repository from an organization to your GitHub account. e.g., ``github.com/scikit-package/scikit-package`` to ``github.com/sbillinge/scikit-package``.

:upstream: The repository of the original source code. e.g., ``github.com/scikit-package/scikit-package``.

:origin: The forked repository under your account. e.g., ``github.com/sbillinge/scikit-package``.

:remote: The repository that is hosted by GitHub. e.g., ``github.com/scikit-package/scikit-package`` or ``github.com/sbillinge/scikit-package``.

:branch: The branch serves as a folder that contains the files of the repository. The ``main`` branch is the branch that is used for the final version of the code. Many branches can be created for different features or bug fixes that are later merged into the ``main`` branch.

:git clone: The process of locally downloading a repository from GitHub (``remote``) to your local machine.

:git push: The process of updating code from the local computer to the GitHub remote repository. Push can be made to the ``origin`` or ``upstream`` repository. But, in our workflow, we push to the ``origin`` repository, and then we create a pull request to merge the changes from ``origin`` to the ``upstream`` repository.

:git commit: The process of adding a description for the changes made in the files that are ready to be pushed.

:git add: The process of selecting files to be included within a single commit.

I have cloned and added ``upstream``. What is the next step?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to first sync our local folder with the ``upstream`` repository. This process is called ``pulling``.

.. code-block:: bash

  git checkout main
  git pull upstream main

Above, we checkout the ``main`` branch of your cloned folder. We then download all the latest changes from the ``upstream`` repository. Recall that a GitHub repository is contributed by multiple contributors. Hence, we want to ensure that we are working with the latest version of the code in the ``main`` branch.

Once we are fully synced with the ``upstream`` repository, we can now start making changes to the code.

Instead of directly working in the ``main`` branch of your cloned repository, you will create a copy of ``main`` by "branching" it from ``main``. Think of a tree. You can name it anything you want like ``docs-faq``, etc.

.. code-block:: bash

  git checkout -b docs-faq

The above command not only creates a new branch but also switches to the new branch. You can verify that you are in the new branch by running:

.. code-block:: bash

  git branch

Of course, you can always switch back to the ``main`` branch by using ``git checkout main``.

Now, you are ready to make changes to the code in the branch. If you have a README file in your project, try to modify it. Once you are done, you want to add the changes to a hidden folder called ``.git``. This process is called ``staging``.

.. code-block:: bash

  git add README.rst

Then, now you want to commit the changes with a message describing the changes.

.. code-block:: bash

  git commit -m "docs: added a FAQ section in the README"

Now, you want to push the changes to the ``origin`` repository under your account. Recall ``origin`` refers to the forked repository under your account hosted by GitHub.

.. code-block:: bash

  git push --set-upstream origin docs-FAQ

Go to your forked repository under your account on GitHub. You will see a green button that says "Compare & pull request". Click on it. You will see the changes you made in the branch. Click on "Create pull request". Add a description of the changes you made. Click on "Create pull request".

The reviewer will review the changes and merge them into the ``upstream`` repository. You have successfully made your first contribution to the organization's repository.

I still need to make another pull request. How do I do that?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, you want to make another pull request. You want to make sure that you are working with the latest version of the code in the ``main`` branch.

.. code-block:: bash

  git checkout main
  git pull upstream main

The command above will sync your local folder with the ``upstream`` repository. It should download the changes made by other contributors as well as the recent commit you made in the ``docs-FAQ`` branch, for example.

Again, you checkout a new branch from the ``main`` branch. You can name it anything you want, e.g. ``docs-typo``.

.. code-block:: bash

  git checkout -b docs-typo

You repeat the process of git add, commit, push to your ``origin`` (your forked repository) and then make a PR to the ``upstream`` repository (the organization's repository).

.. _faq-github-news-automate:

How can I automate the process of creating a new file from the command line?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the following line to ``~/.bashrc`` or ``~/.zshrc`` file:

.. code-block:: bash

    alias cpnews="cp news/TEMPLATE.rst news/$(git rev-parse --abbrev-ref HEAD).rst"

Optionally, if you also want to apply ``git add`` for the ``news/<branch-name>.rst`` created, you can use the following command instead:

.. code-block:: bash

    alias cpnews='cp news/TEMPLATE.rst news/$(git rev-parse --abbrev-ref HEAD).rst && git add news/$(git rev-parse --abbrev-ref HEAD).rst'

Run the following command to apply the shell configuration:

.. code-block:: bash

    source ~/.bashrc

Now, whenever you want to create a news file for the PR, simply navigate to the top-level directory in the project and type ``cpnews`` on the command line.

You can then open the project in an editor. The news file located under ``news`` will have the name ``<branch-name>.rst`` where ``<branch-name>`` is replaced by the current branch name.

Add a description of the edits made in this PR. This should be a user-facing high-level summary of the edits made in this PR and will be automatically converted into the ``CHANGELOG.rst`` when the code is released.

.. seealso::

      How do I write good news items? What if the changes in the PR are trivial and no news is needed? Please read our guide provided in :ref:`news-item-practice`.


Maintaining ``scikit-package``
------------------------------

When should we expect different Python versions to be supported in the GitHub workflows?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please check the **Support Window** section in the official Scientific Python specification: https://scientific-python.org/specs/spec-0000/

Which files should be modified when there is a new Python version?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When updating Python version support, please modify the following files accordingly:

In https://github.com/scikit-package/scikit-package:

.. list-table::
   :header-rows: 1

   * - File
     - Variables to update
   * - ``docs/source/conf.py``
     - ``PYTHON_DEFAULT_MAX_VERSION`` and ``PYTHON_DEFAULT_MIN_VERSION``

In https://github.com/scikit-package/release-scripts:

.. list-table::
   :header-rows: 1

   * - Workflow file
     - Key to update
   * - ``.github/workflows/_matrix-and-codecov-on-merge-to-main.yml``
     - ``python_versions``
   * - ``.github/workflows/_matrix-no-codecov-on-merge-to-main.yml``
     - ``python_versions``
   * - ``.github/workflows/_publish-docs-on-release.yml``
     - ``python_version``
   * - ``.github/workflows/_check-news-item.yml``
     - ``python_version``
   * - ``.github/workflows/_build-pure-python-package.yml``
     - ``python-version``
   * - ``.github/workflows/_tests-on-pr.yml``
     - ``python_version``
   * - ``.github/workflows/_tests-on-pr-no-codecov.yml``
     - ``python_version``
   * - ``.github/workflows/_tests-on-pr-no-codecov-no-headless.yml``
     - ``python-version``
