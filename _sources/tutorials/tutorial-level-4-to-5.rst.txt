.. _level-4-to-5-tutorial:

Migrate your package from Level 4 to Level 5
============================================

Overview
---------

In this guide, you will learn to migrate your package from Level 4 to Level 5. Once you have your package up to the Level 5 standard, you can share your code with the world.

What's the difference between Level 4 and Level 5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Besides the final goal of releasing your package, you will also have the following features:

- Develop documentation with Sphinx with live loading.
- Host documentation on a public URL with GitHub Pages.
- Use GitHub tags to release your package to GitHub and PyPI.
- Maintain changelogs and release notes automatically for each version.

Prerequisites
^^^^^^^^^^^^^

We assume you have already completed and created your scientific code in Level 4, where you have a lightweight Python package that can be installed locally and have your project hosted on GitHub.

.. include:: ../snippets/scikit-installation.rst

Create a new Level 5 project and migrate files
----------------------------------------------

The first step is to create a new project with ``scikit-package`` using the Level 5 ``public`` template. Then we will migrate the files and folders from the existing Level 4 project to the new Level 5 project. Let's begin!


Create a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Visit your project directory and sync with the latest version of the main branch:

    .. code-block:: bash

        cd <project-name>
        git checkout main
        git pull origin main

#. Create a new project with ``scikit-package`` using the Level 5 ``public`` template:

    .. code-block:: bash

        package create public

    .. important::

       We will not run ``git add`` or ``git commit`` on the ``main`` branch at this stage. You will create a new branch called ``skpkg-public`` in a later section, as described in :ref:`level-5-tutorial`. Don't worry! You will be guided through the process.

#. Answer the following questions:

    .. include:: ../snippets/user-input-level-5.rst

#. Enter into the Level 5 project directory:

    .. code-block:: bash

        cd <package-name>

#. Check that you have the following nested folder structure. Here is the structure. We will go through each file and folder:

    .. code-block:: text

        <package-name>     # (Level 4)
        └── <package-name> # (Level 5)
            ├── AUTHORS.rst
            ├── CHANGELOG.rst
            ├── CODE-OF-CONDUCT.rst
            ├── LICENSE.rst
            ├── MANIFEST.in
            ├── README.rst
            ├── docs
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

Migration files from Level 4 to Level 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Enter into the nested Level 5 project directory:

    .. code-block:: bash

        cd <package-name>

#. Move the local ``git`` repository from the Level 4 (``..``) to the Level 5 folder (``.``):

    .. code-block:: bash

        mv ../.git .

#. Move the ``src`` and ``tests`` folders from Level 4 to Level 5:

    .. code-block:: bash

        cp -n -r ../src .
        cp -n -r ../tests .

#. Copy the requirements files from Level 4 to Level 5:

    .. code-block:: bash

        cp ../requirements/conda.txt ./requirements/conda.txt
        cp ../requirements/pip.txt ./requirements/pip.txt
        cp ../requirements/tests.txt ./requirements/tests.txt

#. At this point, you should be able to install the package locally and test it using your existing conda environment:

    .. code-block:: bash

        conda activate  <package-name>-env
        pytest tests

#. Once the tests pass, let's manually migrate hand-written files like ``README.md`` from Level 4 to Level 5.

    .. note::

        In Level 5, we provide a rich template for ``README.rst`` instead of using ``README.md``. If you already had a rich ``README.md`` in Level 4, you can use a tool to convert ``.md`` to ``.rst``. For example, you may use this free `CloudConvert <https://cloudconvert.com/md-to-rst/>`_ tool.

Build documentation locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``/docs`` is the the Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.

.. include:: ../snippets/doc-local-build.rst

What's next?
------------

Let's setup advanced GitHub Actions to automate code linting and testing and upload to the GitHub repository using a pull request from the ``skpkg-public`` branch to ``main``. Please continue the rest of the Level 5 tutorial starting from :ref:`tutorial-level-5-github-setup`.
