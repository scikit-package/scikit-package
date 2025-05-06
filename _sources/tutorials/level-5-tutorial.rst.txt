.. _level-5-tutorial:

(Level 5) Share code as a publicly installable Python package
--------------------------------------------------------------


Overview
^^^^^^^^

In this guide, you will learn to migrate your package from Level 4 to Level 5. Once you have your package up to the Level 5 standard, you can share your code with the world.

Prerequisites
^^^^^^^^^^^^^

You have already completed and created your scientific code in Level 4, where you have a lightweight Python package that can be installed locally and have your project hosted on GitHub.

What's the difference between Level 4 and Level 5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Besides the final goal of releasing your package, you will also have the following features:

- Develop documentation with Sphinx with live loading.
- Host documentation on a public URL with GitHub Pages.
- Use GitHub tags to release your package to GitHub and PyPI.
- Maintain changelogs and release notes automatically for each version.

Create a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure you have the latest version of ``scikit-package`` installed as shown in Level 4.

.. include:: ../snippets/scikit-installation.rst


.. _level-5-new-project:

Create a new project folder with ``scikit-package`` using the Level-5 ``public`` template.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Visit your project directory and sync with the latest version of the main branch.

    .. code-block:: bash

        $ cd <project-name>
        $ git checkout main
        $ git pull origin main

#. Create a new branch where you will initiate a new project.

    .. code-block:: bash

        $ git checkout -b skpkg-public

#. Create a new project with ``scikit-package`` using the Level-5 ``public`` template.

    .. code-block:: bash

        $ package create public

#. Answer the following questions:

.. include:: ../snippets/user-input-level-5.rst

Enter the new folder
^^^^^^^^^^^^^^^^^^^^

#. Enter into the Level 5 project directory.

    .. code-block:: bash

        $ cd my-package

#. Check that you have the following nested folder structure. Here is the structure. We will go through each file and folder.

    .. code-block:: text

        my-package     # (Level 4)
        └── my-package # (Level 5)
            ├── AUTHORS.rst
            ├── CHANGELOG.rst
            ├── CODE_OF_CONDUCT.rst
            ├── LICENSE.rst
            ├── MANIFEST.in
            ├── README.rst
            ├── doc
            ├── news
            ├── pyproject.toml
            ├── requirements
            ├── src
            └── tests
        ├── LICENSE.rst
        ├── README.md
        ├── pyproject.toml
        ├── requirements
        ├── src
        └── tests

Migration code from Level 4 to Level 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Move the local ``git`` repository from the Level 4 to the Level 5 folder.

    .. code-block:: bash

        $ mv ../.git .

#. Move the ``src`` and ``tests`` folders from Level 4 to Level 5.

    .. code-block:: bash

        $ cp -n -r ../src .
        $ cp -n -r ../tests .

#. Copy the requirements files from Level 4 to Level 5.

    .. code-block:: bash

        $ cp ../requirements/conda.txt ./requirements/conda.txt
        $ cp ../requirements/pip.txt ./requirements/pip.txt
        $ cp ../requirements/test.txt ./requirements/test.txt

#. At this point, you should be able to install the package locally and test it.

    .. code-block:: bash

        $ pip install -e .
        $ pytest

#. Once the tests pass, let's manually migrate hand-written files like ``README.md`` from Level 4 to Level 5.

    .. note::

        In Level 5, we provide a rich template for ``README.rst`` instead of using ``README.md``. If you already had a rich ``README.md`` in Level 4, you can use a tool to convert ``.md`` to ``.rst``. For example, you may use this free `CloudConvert <https://cloudconvert.com/md-to-rst/>`_ tool.

#. Done!

Build documentation locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``/doc`` is the the Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.

.. include:: snippets/doc-local-build.rst


Upload your code to GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Let's now add all the files and folders to the GitHub repository.

#. Since the template is expected to work out of the box from Level 4 to 5, we can simply git add all the files and folders to the GitHub repository.

    .. code-block:: bash

        $ git add .
        $ git commit -m "skpkg: migrate from Level 4 to Level 5"
        $ git push --set-upstream origin skpkg-public

#. Let's not migrate our code to the ``main`` branch just yet since mistakes could happen. Let's create a new branch called ``skpkg-migration``.

#. Visit your GitHub repository. On the main page, notice the ``main`` branch clickable button, and it says, ``Find or create a branch``.

#. Enter ``skpkg-migration`` in the text box. Click on the ``Create branch: skpkg-migration from main`` button.

#. Create a PR from ``skpkg-public`` to a new branch called ``skpkg-migration``.

#. Set the PR title as ``skpkg: migrate from Level 4 to Level 5``.

    .. note::

        There are some important files and folders that are different from Level 4. Don't worry about them. We will go through them one by one for each section throughout the guide.

#. Expect ``tests-on-PR`` to fail while ``pre-commit CI`` works.

#. Merge the PR to the ``skpkg-migration`` branch. It's okay that the CI fails. We will fix it in the following section.

#. Let's fix the ``Codecov`` CI error in the following section.

Setup Codecov token for GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-codecov-setup.rst

Allow GitHub Actions to write comments in PRs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As you will see in the next section, we'd like to have GitHub Actions write comments such as warnings. Let's specify the permissions in the GitHub repository settings by following the steps below.

#. Visit the :guilabel:`Settings` page of the GitHub repository.

#. Click on :guilabel:`Actions` in the left sidebar.

#. Click on :guilabel:`General` in the left sidebar.

#. Scroll down to the :guilabel:`Workflow permissions` section.

#. Select :guilabel:`Read and write permissions`.

#. Done!

.. _news-keyboard-shortcut:

Add news items in the GitHub pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before merging to ``main``, we require that each PR includes a file documenting the changes under ``\news``. This ensures that the changes are documented in the ``CHANGELOG.rst`` when you create a new release, as shown in https://billingegroup.github.io/scikit-package/release.html, for example.

    .. important::

        If no news file is created for this PR, the CI will not only fail but also write a comment to remind you to create a news file. Recall we granted GitHub Actions permission to write comments in the PR in the previous section.

Let's create a news item for the changes made in this PR.

#. Get the latest updates from the remote GitHub repository.

    .. code-block:: bash

        $ git fetch --all

#. Check out the ``skpkg-migration`` branch and sync with the remote branch.

    .. code-block:: bash

        $ git checkout skpkg-migration
        $ git pull origin skpkg-migration

#. Make a copy of ``news/TEMPLATE.rst`` and rename to ``news/<branch-name>.rst``.

#. (optional) If you are using a Linux shell, you can setup an ``alias`` to make the creation of the news file ready for editing much quicker and easier:


    Add the following line to ``~/.bashrc`` or ``~/.zshrc`` file:

    .. code-block:: bash

        $ alias cpnews="cp news/TEMPLATE.rst news/$(git rev-parse --abbrev-ref HEAD).rst"

    Run the following command to apply the shell configuration.

    .. code-block:: bash

        $ source ~/.bashrc  # if you are using bash
        $ source ~/.zshrc  # if you are using zsh

    Now, whenever you want to create a news file, simply navigate to the top-level directory in the project and type ``cpnews`` on the command line.

    You can then open the project in an editor. The news file located under ``news`` will have the name ``<branch-name>.rst`` where ``<branch-name>`` is replaced by the current branch name.

    Add a description of the edits made in this PR. This should be a user-facing high-level summary of the edits made in this PR and will be automatically converted into the ``CHANGELOG.rst`` when the code is released.

    .. note::

        How do I write good news items? What if the changes in the PR are trivial and no news is needed? Please check out the news guide in the FAQ :ref:`here<news-item-practice>`.


#. Do not delete ``news/TEMPLATE.rst``. Leave it as it is.

#. Do not modify other section headers in the rst file. Replace ``* <news item>`` with the following item:

    .. code-block:: text

        **Added:**

        * Support public releases with scikit-package by migrating the package from Level 4 to Level 5 in the scikit-package standard.

#. Push the change to the remote GitHub repository.

    .. code-block:: bash

        $ git add news/skpkg-migration.rst
        $ git commit -m "chore: Add news item for skpkg-migration"
        $ git push origin skpkg-migration

Congratulations! You are done with migrating your package from Level 4 to Level 5. You can now start writing docstrings for your Python code and tests for your code. Then, also write good documentation for your code, including Getting Started guides.

    .. important::

        For writing great news items, Python docstrings, tests, and commit messages, check the Billinge research group's guidelines :ref:`here<billinge-group-standards>`.

(Optional) Build API reference documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/api-reference-doc.rst

Ready for public release?
^^^^^^^^^^^^^^^^^^^^^^^^^

Congratulations! Your package has been successfully migrated. This has been the most challenging step. Now, let's release your package to PyPI and conda-forge. Please visit the :ref:`Release your package <release-pypi-github>` page to learn how to release your package!
