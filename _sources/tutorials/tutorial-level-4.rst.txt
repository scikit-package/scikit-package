.. _level-4-tutorial:

(Level 4) Share your code as a locally installable Python package
=================================================================

Overview
--------

In this tutorial, you will learn how to share code across any files in your computer. By the end of this tutorial, you will also have your package hosted on GitHub, where you will utilize GitHub Actions to run automatic linting and testing for the incoming code in your GitHub repository.

This tutorial should take about 10 to 15 minutes.

Table of contents
^^^^^^^^^^^^^^^^^

1. :ref:`create-new-project-with-scikit-package`

2. :ref:`automate-code-linting-and-testing`

3. :ref:`use-pull-request-to-upload-code-to-github`

Prerequisites
^^^^^^^^^^^^^

For Level 4, we assume you have prior experience in developing scientific code in Python.

.. seealso:: Are you new to Git and GitHub?

    Please read the GitHub workflow section in :ref:`faq-github-workflow` to familiarize yourself with the common jargon and terms used. There are also many online resources for learning Git and GitHub.

.. include:: ../snippets/scikit-installation.rst

.. _create-new-project-with-scikit-package:

Step 1. Create a new package with ``scikit-package``
----------------------------------------------------

.. _create-new-github-repo:

Create a new GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this tutorial, we will start by creating a new GitHub repository. The GitHub repository is where we will host our code online (remote).

.. include:: ../snippets/github-create-new-repo.rst

Let's now create a new package in your computer (local) using ``scikit-package``.

Create a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command to create a new project with ``scikit-package``:

    .. code-block:: bash

        package create system

#. Respond to the following prompts:

    .. list-table::
       :header-rows: 1
       :widths: 25 75

       * - Prompt
         - Description and example
       * - project_name
         - The project name. Will be used for the top level folder name. e.g., my-package
       * - github_username_or_orgname
         - Your GitHub username, or GitHub organization name, where it will be hosted on GitHub. e.g., sbillinge or billingegroup
       * - github_repo_name
         - The GitHub repository name. Usually the same as the project_name. Use ``name-with-hypens``. e.g., my-package
       * - conda_pypi_package_dist_name
         - The name displayed on PyPI and conda-forge. Must not already exist there. Use ``name-with-hypens``. e.g., my-package
       * - package_dir_name
         - The name of the package directory under ``src``. Usually the same as the project name  but use ``name_with_underscores``. e.g., my_package
       * - contributors
         - The contributors involved in the project. e.g., Sangjoon Lee, Simon Billinge

    .. note::

        You may press the "Enter" key on your keyboard to accept the default value for the field provided in parentheses.

#. ``cd`` into the project directory created by the ``package create system`` command above. We will assume that the user has entered the project name as ``my-package``.

    .. code-block:: bash

        cd my-package

#. Confirm that you have the following folder structure shown below:

    .. code-block:: text

        my-package/
        ├── LICENSE.rst
        ├── README.md
        ├── pyproject.toml
        ├── requirements
        │   ├── conda.txt
        │   ├── pip.txt
        │   └── tests.txt
        ├── src
        │   └── my_package
        │   ├── __init__.py
        │   └── functions.py
        └── tests
            └── test_functions.py

#. Done! Let's now install your package in your local computer where the code can be used in any Python script or Jupyter notebook.

Install your package locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/package-install-test-local.rst

Upload ``README.md`` to your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-upload-readme-pre-commit.rst

.. _automate-code-linting-and-testing:

Step 2. Automate code linting and testing with GitHub Actions
-------------------------------------------------------------

Setup pre-commit to lint code before making a commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/pre-commit-local-setup.rst

Setup ``pre-commit CI`` in the remote repository in each pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-pre-commit-setup.rst

.. _use-pull-request-to-upload-code-to-github:

Step 3. Upload rest of files to GitHub repository with pull request
-------------------------------------------------------------------

.. include:: ../snippets/github-upload-all-remaining-files-level-4.rst

(Recommended) How to develop your code moving forward using pull requests
-------------------------------------------------------------------------

.. include:: ../snippets/github-workflow-moving-forward.rst

What's next?
------------

Once you are ready to release your package to the wider world, let's proceed to :ref:`level-5-tutorial` where you will learn to release your package to PyPI and conda-forge so that your package can be installed by anyone in the world.
