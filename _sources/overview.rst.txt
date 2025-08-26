:tocdepth: -1

.. index:: overview

.. _overview:

Overview
--------

Here are the 5 levels of sharing your code. We provide tutorials for each level.

.. include:: snippets/5-levels-table.rst

Where do I begin?
-----------------

I am here to **start a new Python** project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ⏩️ If you have **experience** developing scientific code in Python, we recommend starting from Level 4, where you will create a lightweight Python package with automatic formatting and unit testing using GitHub Actions.

        .. code-block:: bash

            conda create -n skpkg-env scikit-package
            conda activate skpkg-env
            package create system

        Follow the prompts to enter information for your package. You may follow the full tutorial provided in :ref:`level-4-tutorial`.

    ⏩️ If you are an **active open-source developer** and are also familiar with GitHub Actions and forking workflows, we recommend you start from Level 5.

        .. code-block:: bash

            conda create -n skpkg-env scikit-package
            conda activate skpkg-env
            package create public

        Follow the prompts to enter information for your package. You may follow the full tutorial provided in :ref:`level-5-tutorial`.

    ⏩️ If you are **new** to programming, start from Level 1. You will learn how to reuse code across files and folders. You will also learn how to write unit tests and use virtual (conda) environments. To get started, visit :ref:`level-1-2-3-tutorials`.

I am interested in **migrating my existing package** to the Level 5 ``public`` standard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Create a new environment with ``scikit-package`` installed:

        .. code-block:: bash

            conda create -n skpkg-env scikit-package black pre-commit
            conda activate skpkg-env

    Assuming a forking workflow, clone the repository and ``cd`` into the package folder:

        .. code-block:: bash

            cd <your-package-folder-path>

    Then, three workflows will be introduced. First, you will lint your existing code using ``pre-commit``. Then, you will migrate the source code, test files, and documentation to the new package directory created with ``package create public``. Finally, you will check the content of the repository, include the license, and conduct functional testing. You may follow the complete step-by-step tutorial provided in :ref:`migrate-existing-package-to-level-5`.

I am interested in supporting Level 5 ``public`` from Level 4 ``system``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    To get started, follow the step-by-step instructions provided in :ref:`level-4-to-5-tutorial`.

I want to publish my **package** on GitHub, PyPI, and conda-forge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    In practice, here is how you can release your package on GitHub and PyPI using GitHub Actions:

        .. code-block:: bash

            git tag <version-number>
            git push upstream <version-number>

    To get started, follow the step-by-step instructions in :ref:`release-pypi-github`. After release, if you want to make your package available on ``conda-forge``, visit :ref:`release-conda-forge`.

I want to explore **best practices** for developing and publishing scientific code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The documentation covers, among other topics, how to write effective Git commit messages and news entries used for compiling the changelog, as well as a recommended workflow for developing and requesting new features within GitHub's ecosystem. To get started, visit :ref:`billinge-group-standards`.
