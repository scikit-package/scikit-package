.. index:: migration-guide

.. _migrate-existing-package-to-level-5:

Migrate your existing package with ``scikit-package``
=====================================================

Prerequisites
-------------

This guide is for developers who have an existing Python package under Git control and want to migrate it to the Level 5 ``scikit-package`` standard.

We assume you have experience creating a package using ``scikit-package`` Level 4 and 5. We also assume you are familiar with the forking workflow on GitHub.

.. seealso:: If you are not familiar with contributing via forking, please read :ref:`faq-github-workflow-overview`.

Tips and how to receive support
-------------------------------

We understand that migration can be challenging. We offer many ways to help you guide through the process:

#. You may cross-check with the Billinge group's up-to-date package, ``diffpy.utils``: https://github.com/diffpy/diffpy.utils.

#. We provide :ref:`frequently-asked-questions` describing  design decisions and how to override them in the ``scikit-package`` template.

#. After you've cross-checked and searched through the documentation (tutorials, examples, FAQs) please feel free to ask questions by creating an issue in the GitHub repository `here <https://github.com/scikit-package/scikit-package/issues>`_.

.. include:: ../snippets/scikit-installation.rst

.. _migration-pre-commit:

Step 1. Pre-commit workflow
---------------------------

#. Clone the repository and set ``upstream`` to the original repository.

    .. code-block::

        git clone <URL-of-the-forked-repo>
        cd <package-name>
        git remote add upstream <URL-of-the-original-repo>

    .. note::

        - Are you the creator of the repository? You can type ``origin`` instead of ``upstream`` in the rest of the tutorial, e.g., ``git pull origin main`` instead of ``git pull upstream main``. Here, we assume a forking workflow.
        - Is your default branch called ``master``? Run ``git pull upstream master`` throughout the guide instead. However, please note that ``main`` is the default branch name for GitHub.


Run ``black`` in your codebase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a new branch called ``black-edits``. This branch will be used to apply ``black`` to all files in the old project directory:

    .. code-block:: bash

        git checkout main
        git pull upstream main


#. Activate the conda environment and install ``black``:

    .. code-block:: bash

        conda activate skpkg-env
        conda install black

#. Create a new branch called ``black-edits`` and create a new file called ``pyproject.toml``:

    .. code-block:: bash

        git checkout -b black-edits

#. If you do not have a ``pyproject.toml`` file, you can create one by running the following command:

    .. code-block:: bash

        touch pyproject.toml

#. Copy and paste the following content at the bottom of ``pyproject.toml``:

    .. code-block:: text

        [tool.black]
        line-length = 79
        include = '\.pyi?$'
        exclude = '''
        /(
            \.git
        | \.hg
        | \.mypy_cache
        | \.tox
        | \.venv
        | \.rst
        | \.txt
        | _build
        | buck-out
        | build
        | dist
        | blib2to3
        | tests/data
        )/
        '''

#. Lint the code:

    .. code-block:: bash

        black .

    .. seealso:: To skip certain files, add them under the ``exclude`` section in the ``pyproject.toml``.

#. Push the changes to the ``black-edits`` branch:

    .. code-block:: bash

        git add .
        git commit -m "skpkg: apply black to all files in the project directory"
        git push origin black-edits

#. Create a PR from ``username/black-edits`` to ``upstream/main``.

    The PR title can be ``skpkg: apply black line-length 79 to all files in the project directory``.

#. Review and wait for the PR to be merged to ``upstream/main``. If you are the project maintainer, you can merge the PR yourself.

#. Done!

Apply pre-commit auto-fixes without manual edits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Sync with the ``upstream/main`` branch:

    .. code-block:: bash

        git checkout main && git pull upstream main

#. Create a new branch called ``pre-commit-auto``:

    .. code-block:: bash

        git checkout -b pre-commit-auto

#. Create a new package using ``scikit-package``:

    .. code-block:: bash

        package create public

#. Copy the ``pre-commit`` configuration files from the new to the old directory:

    .. code-block:: bash

        cp <package-name>/.pre-commit-config.yaml .
        cp <package-name>/.isort.cfg .
        cp <package-name>/.flake8 .

#. Trigger hooks and auto-fixes without manual edits:

    .. code-block:: bash

        pre-commit run --all-files

#. Run ``git status`` to see all the files that have been modified by ``pre-commit`` hooks:

      .. code-block:: bash

          git status

#. When you run ``git status``, you will see the package you created under ``Untracked files`` with the package name you gave. At this step, you want to add and commit everything **except** this package. To do so, run the following commands and replace ``<package-name>`` with the name of your package:

    .. code-block:: bash

        git add -- . ':!<package-name>'
        git commit -m "style: apply pre-commit hooks with no manual edits"

#. Push the changes to the remote repository:

    .. code-block:: bash

        git push origin pre-commit-auto

#. Create a PR from ``username/pre-commit-auto`` to ``upstream/migration``. The PR title can be ``skpkg: apply pre-commit to project directory with no manual edits``.

    .. note::

        The new ``upstream/migration`` branch can be created by the project maintainer or owner. On the main page of the upstream repository, click :menuselection:`main --> Switch branches/tags --> Find or create a branch` and type ``migration``. This will create a new branch called ``migration``.

#. Wait for the PR to be merged to ``upstream/migration`` branch.

Apply manual edits to pass ``pre-commit`` hooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The package will most likely have failed ``pre-commit`` hooks. We will manually fix the errors raised by ``flake8``, ``codespell``, etc.

.. note::

    Do you have **no pre-commit errors** after running ``pre-commit run --all-files``? Great! You can skip this section and move on to the next section.

Here, instead of fixing all errors at once, we will address each type of error one at a time.  For example, a branch called ``pre-commit-spelling`` may contain spelling fixes, while another branch, ``pre-commit-flake8-line`` fixes of line length errors raised by flake8.

#. To get the ``migration`` branch from ``upstream/migration`` and track it, run the following commands:

    .. code-block:: bash

        git fetch upstream migration
        git checkout --track upstream/migration

#. Make sure everything is sync'd with the ``upstream/migration`` branch:

    .. code-block:: bash

        git pull upstream migration

#. Create a new branch that will be used to fix the type of errors like flake8 or codespell:

    .. code-block:: bash

        git checkout -b pre-commit-<theme>

#. Run ``pre-commit run --all-files`` to see the errors:

    .. seealso::

        Do you want to **ignore** certain files/folders and also set the preferred line-length? Visit :ref:`faq-pre-commit` in the FAQ section to learn how to customize line-lenghts, ignore certain errors, and skip certain files and paths.

        If you are suppressing ``flake8`` errors, you can **create GitHub issues** to resolve them after migration.

#. Fix the errors manually for the specific theme.

#. Once you are done with fixing the type of errors commit, push the changes to your branch

    .. code-block:: bash

        git add <files-modified-to-fix-error>
        git commit -m "skpkg: fix <theme> errors"
        git push origin pre-commit-<theme>

#. Create a PR from ``username/pre-commit-<theme>`` to ``upstream/migration``. The PR title can be ``skpkg: fix <theme> errors``.

#. Wait for the PR to be merged to ``upstream/migration`` branch.

#. Repeat for other themes of errors, always pull the latest commits from ``upstream/migration`` before creating a new branch:

    .. code-block:: bash

        git checkout migration
        git pull upstream migration
        git checkout -b pre-commit-<another-theme>

#. Are all the PRs merged and do all ``pre-commit`` hooks pass? If so, you are ready for the next section! Before that, let's automatically trigger ``pre-commit`` hooks going forward:

    .. code-block:: bash

        pre-commit install

Setup pre-commit CI
^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-pre-commit-setup.rst

.. _migration-workflow:

Step 2. Migration workflow
--------------------------

Let's first migrate the essential files from the old project to the new project directory.

.. Attention:: Please read the following carefully before proceeding:

    - Please Do NOT delete/remove any files before confirming that it is absolutely unnecessary. If you are unsure, contact the project maintainer first.

    - Please Do NOT delete project-specific content such as project descriptions in README, license information, authors, tutorials, examples.

Move essential files to run local tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Pull the latest commits from ``upstream/migration``

    .. code-block::

        git checkout migration && git pull upstream migration

#. Move into the new directory created by ``scikit-package``:

    .. code-block::

        cd <package-name>

#. Move ``.git`` from the old (``..``) to the new directory (``.``):

    .. code-block::

        mv ../.git .

#. See a list of files that have been (1) untracked, (2) deleted, (3) modified:

    .. code-block::

        git status

    .. seealso::

        - ``untracked`` are new files created by ``scikit-package``.
        - ``deleted`` are files in the old directory but the files that are not in the new directory. At the moment, most of the ``src`` and ``tests`` and ``doc`` files will be in this category. We will move them from the old to the new directory in the next few steps.
        - ``modified`` are files that that exist both in the old and the new directory, while the scikig-package has made changes to them.

#. Create a new branch called ``setup-CI``:

    .. code-block:: bash

        $ git checkout -b setup-CI

#. Now you will move ``src`` and ``tests`` folders in the following steps.

#. Copy files

    .. code-block:: bash

        cp -n -r ../src/* src/
        cp -n -r ../tests/* tests/

    .. seealso::

        The ``-n`` option is used to prevent overwriting existing files in the destination directory. If you want to overwrite existing files, remove the ``-n`` option.

#. Confirm the ``src`` and ``tests`` files that showed as ``deleted`` are no longer in the ``deleted``.

    .. code-block:: bash

        git status

    .. attention::
        If you see any files under ``src`` or ``tests`` that are modified, **manually check these files** and decide whether you want to keep the changes made by ``scikit-package`` or not.

#. By default, ``scikit-package`` generates an example source file, test file, and documentation file. If you do not need these files, you can delete them:

    .. code-block:: bash

        rm src/<package-name>/functions.py
        rm tests/test_functions.py
        rm docs/source/api/<package-name>.example_package.rst

#. If any files have been added or modified in the way you like, you can add and commit the changes. Otherwise, you can skip this step:

    .. code-block:: bash

        git add src && git commit -m "skpkg: migrate src folder"
        git add tests && git commit -m "skpkg: migrate tests folder"

#. Manually list the dependencies under ``requirements/pip.txt``, ``requirements/tests.txt``, ``requirements/docs.txt``, ``requirements/conda.txt``, and ``requirements/build.txt`` (see below for more details on this file).

   - ``pip.txt``
     Core runtime dependencies needed to use the package.

   - ``tests.txt``
     Packages required for running tests and checking coverage.

   - ``docs.txt``
     Dependencies for building documentation.

   - ``conda.txt``
     Base environment packages best installed via ``conda``.
   - ``build.txt`` *(optional)*
     Build tools needed for non-Python components (e.g., C/C++ libraries, compilers). Only include if your package requires compilation.

#. Delete ``requirements/build.txt`` if your package only contains Python code.

    .. code-block:: bash

        rm requirements/build.txt

#. Add and commit the changes in the  ``requirements`` folder:

    .. code-block:: bash

        git add requirements
        git commit -m "skpkg: list dependencies in requirements folder"

#. Test your package from a new conda environment:

    .. code-block:: bash

        conda create -n <package-name>-env python=3.13 \
            --file requirements/conda.txt \
            --file requirements/tests.txt
        conda activate <package-name>-env
        pip install -e . --no-deps
        pytest

    .. note::

        Include ``--file requirements/build.txt`` if it exists.

#. Congratulations! After the tests pass, let's now setup GitHub Actions in the following section.

Setup repository
^^^^^^^^^^^^^^^^

We want to run GitHub Actions, in order to do so

- :ref:`tutorial-5-pre-commit-ci`
- :ref:`tutorial-5-github-codecov-setup`
- :ref:`tutorial-5-ci-permission`

Setup GitHub Actions
^^^^^^^^^^^^^^^^^^^^

#. Add and commit the files in the ``.github`` folder:

    .. code-block:: bash

        git add .github/workflows/tests-on-pr.yml .gitignore
        git commit -m "skpkg: add CI and issue/PR templates"

    .. Attention::
        If your package does not support the latest Python version of |PYTHON_MAX_VERSION|, you will need to specify the Python version supported by your package. Follow the instructions here to set the Python version under ``.github/workflows`` in :ref:`faq-github-actions-python-versions`.


    .. seealso::
        If you need to run **extra CLI commands in the GitHub workflow** for running tests, you can refer to :ref:`faq-github-actions-extra-cli-commands`. For example, you may want to run ``pip install <package-name>`` because the package is not available on conda-forge yet available on PyPI only.

#. Add and commit the ``requirements`` folder:

    .. code-block:: bash

        $ git add requirements
        $ git commit -m "skpkg: list dependencies in requirements folder"

#. Add and commit ``pyproject.toml``:

    .. code-block:: bash

        $ git add pyproject.toml
        $ git commit -m "skpkg: add pyproject.toml"

#. Push the changes to the ``setup-CI`` branch:

    .. code-block:: bash

        $ git push origin setup-CI

#. Create a PR from ``username/setup-CI`` to ``upstream/migration``.

    The pull request title can be ``skpkg: setup CI after migrating tests, src, requirements, and .github folder``.

#. Wait for review after CI passes.

#. Once the PR is merged, let's upload other files.

Add configuration files
^^^^^^^^^^^^^^^^^^^^^^^

#. Pull the latest commits from ``upstream/migration`` and create a new branch called ``config``:

    .. code-block:: bash

        git checkout migration
        git pull upstream migration
        git checkout -b config

#. Add and commit configuration files:

    .. code-block:: bash

        git add .pre-commit-config.yaml .codespell .flake8 .isort.cfg
        git commit -m "skpkg: add config files for pre-commit "
        git add .readthedocs.yaml .codecov.yml .github
        git commit -m "skpkg: add config files readthedocs, codecov, GitHub"

#. Create a PR from ``username/config`` to ``upstream/migration``.

    The PR title can be ``skpkg: add configuration files for pre-commit, readthedocs, codecov``.

#. Once the PR is merged, move to the next section.

Move documentation files
^^^^^^^^^^^^^^^^^^^^^^^^

#. Pull the latest commits from ``upstream/migration`` and create a new branch called ``doc``:

    .. code-block:: bash

        git checkout migration
        git pull upstream migration
        git checkout -b doc

#. Copy documentation from the old to the new repository:

    .. code-block:: bash

        cp -n -r ../docs/source/* ./docs/source

    .. note::

        If files are moved to a different path like ``docs/manual/source`` (old) to ``docs/source`` (new), open the project in IDE and do a global search (ctrl + shift + f) for ``../`` or ``..`` and modify all relative path instances.

#. Once again, ``scikit-package`` creates template files in the ``docs/source`` folder. If you do not need these files, you can delete them:

    .. code-block:: bash

        rm docs/source/getting-started.rst
        rm -r docs/source/img/
        rm -r docs/source/snippets/

#. Some files in ``docs/source`` may have been modified by ``scikit-package``. Manually check these files and decide whether you want to keep the changes made by ``scikit-package`` or not. After doing this, you can add and commit changes (if applicable):

    .. code-block:: bash

        git add docs/source
        git commit -m "skpkg: migrate docs/source files"

#. Ensure the documentation can be built locally:

    .. code-block:: bash

        conda install --file requirements/docs.txt
        cd docs && make html && open build/html/index.html


#. Add and commit the changes:

    .. code-block:: bash

        git add docs
        git commit -m "skpkg: migrate documentation"

#. By hand, migrate content over to ``README.rst``.

    .. note::

        In Level 5, we provide a rich template for ``README.rst`` instead of using ``README.md``. If you already had a rich ``README.md`` in Level 4, you can use a tool to convert ``.md`` to ``.rst``. For example, you may use this free `CloudConvert <https://cloudconvert.com/md-to-rst/>`_ tool.

#. Add other public facing static files:

    .. code-block:: bash

        git add AUTHORS.rst CHANGELOG.rst CODE-OF-CONDUCT.rst LICENSE.rst
        git commit -m "skpkg: add config files for authors, changelog, code of conduct, license"
        git add MANIFEST.in
        git commit -m "skpkg: add MANIFEST.in"
        git add README.rst
        git commit -m "skpkg: add README.rst"

#. Create a news file:

    .. code-block:: bash

        cp news/TEMPLATE.rst news/doc.rst

#. In ``news/docs..rst``, add the following content under ``Fixed:``:

    .. code-block:: text

        **Added:**

        * <news item>

        **Fixed:**

        * Support ``scikit-package`` Level 5 standard (https://scikit-package.github.io/scikit-package/).

    .. seealso::

        To streamline the above steps, you may instead run ``package add news --fix -m "Support scikit-package Level 5 standard."``. For more, please refer to :ref:`news-item-practice`.

#. Add the news files:

    .. code-block:: bash

        git add news
        git commit -m "skpkg: add news files"

#. Create a PR from ``username/doc`` to ``upstream/migration``.

    The PR title can be ``skpkg: migrate documentation, README, and public static files``.

#. Once the PR is merged to ``upstream/main``, move to the final step!

Step 3. Final check
-------------------

#. Review the following items:

    - All the badges on ``README.rst`` are passing.
    - ``LICENSE.rst`` is verified as correct.
    - Locally rendered documentation contains all appropriate pages, tutorials, and other human-written text is up-to-date with any changes in the code.
    - Installation instructions in the ``README.rst``, documentation, and the website are updated.
    - Successfully run any tutorial examples or do functional testing with the latest Python version.
    - Grammar and writing quality are checked (no typos).

#. Ask the project maintainer to create a PR from ``upstream/migration`` to ``upstream/main``

#. After the PR is merged to ``upstream/main``, archive the old repository by changing its name:

    .. code-block:: bash

        cd ..
        mv <package-name> <package-name>-archive

#. Clone the latest version of the package from the remote:

    .. code-block:: bash

        cd ~/dev
        git clone <URL-of-the-forked-repo>
        git remote add upstream <URL-of-the-original-repo>
        git pull upstream main

#. Now, you should be able to run the following to test your package!

    .. code-block:: bash

        conda activate <package-name>-env
        pytest
        pre-commit run --all-files

#. Congratulations! You are done with migration!

Ready for release?
------------------

Are you ready to release your package to PyPI and conda-forge? Let's start from :ref:`release-pypi-github`!
