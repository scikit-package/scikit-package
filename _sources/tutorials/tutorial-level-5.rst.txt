.. _level-5-tutorial:

(Level 5) Share your code as a publicly installable package
===========================================================

Overview
--------

Welcome! By the end of the tutorial, you will be able to share your code as a publicly installable package that can be installed using ``pip install <package-name>`` and ``conda install <package-name>``.

Prerequisites
^^^^^^^^^^^^^

We assume that you have a basic understanding of starting a new project and have hosted at least one project on GitHub. If you are new to GitHub, we recommend you start from :ref:`level-4-tutorial` where you will learn how to create a new project and host it on GitHub while using GitHub Actions to automatically format your code and run unit tests.

Make sure you have the latest version of ``scikit-package`` installed:

.. include:: ../snippets/scikit-installation.rst

.. _level-5-tutorial-new-project:


Step 1. Create a new project with ``scikit-package``
----------------------------------------------------

Create a new GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-create-new-repo.rst

Create a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command to create a new project folder with ``scikit-package`` using the Level 5 ``public`` template:

    .. code-block:: bash

        package create public

#. Answer the following questions:

    .. include:: ../snippets/user-input-level-5.rst

    .. note::

        You may press the "Enter" key to accept the default values for the questions.

#. Now type ``ls`` to check a new folder has been created.

Install your package locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/package-install-test-local.rst

Build documentation locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``/docs`` is the the Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.

.. include:: ../snippets/doc-local-build.rst

Upload ``README.md`` to your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-upload-readme-pre-commit.rst

.. _tutorial-level-5-github-setup:

Step 2. Automate code linting and testing with GitHub Actions
-------------------------------------------------------------

We will do 3 things in order to automate testing, linting, infrastructure in your GitHub repository. Rest assured that these configuration steps are only done once!

- :ref:`tutorial-5-pre-commit-ci`
- :ref:`tutorial-5-github-codecov-setup`
- :ref:`tutorial-5-ci-permission`

The above steps will take 5 to 10 minutes in total but save hours and days of time in the long run.

.. _tutorial-5-pre-commit-ci:

1. Setup ``pre-commit CI`` in the remote repository in each pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-pre-commit-setup.rst

.. _tutorial-5-github-codecov-setup:

2. Setup Codecov token for GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-codecov-setup.rst

.. _tutorial-5-ci-permission:

3. Allow GitHub Actions to write comments in PRs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-ci-permission.rst

.. _github-news-item-PR:

Step 3. Upload rest of files to GitHub repository with pull request and news item
----------------------------------------------------------------------------------

Upload remaining files
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-upload-all-remaining-files-level-5.rst

Add news items in the GitHub pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before merging to ``main``, we require that each PR includes a file documenting the changes under ``\news``. This ensures that the changes are documented in the ``CHANGELOG.rst`` when you create a new release, as shown in https://scikit-package.github.io/scikit-package/release.html, for example.

    .. important::

        If no news file is created for this PR, the CI will not only fail but also write a comment to remind you to create a news file. Recall we granted GitHub Actions permission to write comments in the PR in the previous section.

Let's create a news item for the changes made in this PR.

#. Check out the ``skpkg-public`` branch and sync with the remote branch.

    .. code-block:: bash

        git pull origin skpkg-public

#. Make a copy of ``news/TEMPLATE.rst`` and rename to ``news/<branch-name>.rst``.

#. Do not delete ``news/TEMPLATE.rst``. Leave it as it is.

#. Do not modify other section headers in the rst file. Replace ``* <news item>`` with the following item:

    .. code-block:: text

        **Added:**

        * Support public releases with scikit-package by migrating the package from Level 4 to Level 5 in the scikit-package standard.

    .. seealso::

        To streamline the above steps, you may instead run ``package add news --add -m "Support public releases with scikit-package by migrating the package from Level 4 to Level 5 in the scikit-package standard."``. For more, please refer to :ref:`news-item-practice`.

#. Push the change to the remote GitHub repository.

    .. code-block:: bash

        git add news/skpkg-public.rst
        git commit -m "chore: Add news item for skpkg-public"
        git push origin skpkg-public

Create a pull request
^^^^^^^^^^^^^^^^^^^^^

#. In your GitHub repository, click :guilabel:`Compare & pull request`.

#. Set the PR title as ``skpkg: start a new project with Level 5 tutorial``.

#. The ``base`` branch should be ``main`` and the ``compare`` branch should be ``skpkg-public``.

#. Click :guilabel:`Create pull request`.

#. Wait all GitHub Action workflows to run including ``Test on PR``.

#. Also wait for ``pre-commit`` CI to run and pass.

    .. note:: Did ``pre-commit CI`` fail?

        If the pre-commit failed, you will need to first pull the new commit created by ``pre-commit CI`` before making any new edits locally. You can do this by running the following command:

        .. code-block:: bash

         git pull origin skpkg-public

        If you have more problems, please read the FAQ section on :ref:`faq-pre-commit-error`.

#. Click :guilabel:`Files changed` in the PR to to review the new files added to the repository.

#. Once reviewed, click :guilabel:`Merge pull request`.

#. Delete the remote branch after merging.

#. Visit your GitHub repository and confirm that the ``main`` branch is updated.

#. Congratulations! You are done with creating a Level 5 project with ``scikit-package``.

Ready for public release?
-------------------------

Congratulations! Let's release your package to PyPI and conda-forge. Visit :ref:`release-pypi-github` to have your package available via ``conda install`` and ``pip install``!

(Recommended) How to develop your code moving forward using pull requests
-------------------------------------------------------------------------

.. include:: ../snippets/github-workflow-moving-forward.rst


(Optional) Useful features available in Level 5
-----------------------------------------------

.. include:: ../snippets/level-5-optional-sections.rst
