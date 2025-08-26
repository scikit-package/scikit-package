.. _release-conda-forge:

=====================================
Create conda package with conda-forge
=====================================

.. _conda-create-feedstock:

Overview
--------

⏩️ I am new to conda-forge. I just released my package to PyPI/GitHub by following the instruction in :ref:`release-pypi-github`.

     Please get started in :ref:`conda-forge-release-tutorial`.

⏩️ I already have a conda-forge feedstock. It is my **first** time making a new conda package version.

    Please get started in :ref:`conda-forge-feedstock-release`.

⏩️ I already have a conda-forge feedstock. It's **NOT** my first time updating the package version. Can I automate this process?

    Yes! You can run the ``package update conda-forge`` command to prepare a PR for you. Please get started in :ref:`conda-forge-pr-automate`.

.. _conda-forge-release-tutorial:

Create conda package for the frst time
--------------------------------------

Here, you will learn how to release a conda package distributed through the ``conda-forge`` channel in 10 to 15 minutes so that you package can be installed using ``conda install <package-name>``. This guide assumes you are familiar with a basic clone, fork, and pull request workflow on GitHub.

Overview
^^^^^^^^

The process is divided into three steps:

:ref:`conda-forge-recipe-prepare`

    You will learn to prepare package information in a file called ``meta.yaml`` using our ``scikit-package`` template. The file serves as a recipe for building your conda package. The recipe contains the package version, the source code, the dependencies, the license, etc.

:ref:`conda-forge-recipe-upload`

    Once you have the ``meta.yaml`` generated, you will create a pull request to the the `staged-recipes repository <https://github.com/conda-forge/staged-recipes>`_ from your forked repository. The staged-recipes repository is a temporary location for the recipe until it is approved by the conda-forge community.

:ref:`conda-forge-recipe-review`

    One of the community members of conda-forge will review your ``meta.yaml`` and provide feedback. Once the recipe is approved, you will have a package available for ``conda install`` automatically, and you will have your own designated feedstock repository that contains ``meta.yaml`` in ``https://github.com/conda-forge/<package-name>-feedstock``.

.. _conda-forge-recipe-prepare:

Step 1. Prepare conda package recipe in ``meta.yaml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We first need to generate a "recipe" for the conda package. The recipe contains the type of programming language, the package version, the source code, the dependencies, and license, etc. This recipe is stored in a file called ``meta.yaml``.

.. seealso::

    Do you want to learn more about ``meta.yaml``? Please read :ref:`meta-yaml-info`.

Hence, in Step 1, we will generate ``meta.yaml`` using the ``scikit-package`` conda-forge template. See https://github.com/conda-forge/diffpy.utils-feedstock/blob/main/recipe/meta.yaml as an example of a ``meta.yaml`` used in production.

#. Run ``package create conda-forge``

#. Answer the following questions:

    :github_username_or_orgname: The GitHub username or organization name.

    :package_import_name: The name of the module.

    :github_repo_name: The name of the repository.

    :version: The version of the package.

    :min_python_version: The minimum version of Python required. i.e., |PYTHON_MIN_VERSION|

    :project_short_description: The short description of the project.

    :project_full_description: The full description of the project.

    :license_file: The license file located in the package repository. i.e., ``LICENSE.rst``.

    :recipe_maintainers: The GH usernames who can merge PRs in the feedstock.

    :build_requirements: Copy ``requirements/build.txt`` from the project repo.

    :host_requirements: Use the default values provided for pure Python packages.

    :runtime_requirements: Copy from  ``requirements/conda.txt``.

    :testing_requirements: Copy from ``requirements/tests.txt``.

#. ``cd`` into the new directory created by ``scikit-package``.

#. Check ``meta.yaml`` exists.

#. If your package contains only pure Python code, the ``build:`` section **below** the ``requirements:`` section should be empty.

#. If it is empty, remove the ``build:`` under the ``requirements:`` section and confirm that the modified ``meta.yaml`` looks as follows:

    .. code-block:: yaml

        build:
          noarch: python
          number: 0
          script: {{ PYTHON }} -m pip install --no-deps --ignore-installed .

        requirements:
          host:
            - python {{ python_min }}
            - setuptools
            - setuptools-git-versioning >=2.0
            - pip

    Ensure that the ``build:`` section **above** the ``requirements:`` section is not removed.

#. Double-check the license file name in ``meta.yaml`` against the license files in the project repository. If you are unsure, please confirm with the project owner.

#. Done!

.. _conda-forge-recipe-upload:

Step 2. Upload ``meta.yaml`` to conda-forge for initial review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Fork https://github.com/conda-forge/staged-recipes and clone your forked repository.

#. cd into ``staged-recipes``.

#. Create ``recipes/<package-name>/meta.yaml`` Ex) ``recipes/diffpy.srreal/meta.yaml``.

#. Copy and paste the content of ``meta.yaml`` from Step 1.

#. Create a new branch: ``git checkout -b <project_name>``.

#. Add and commit the changes: ``git add . && git commit -m "Committing recipe for conda-forge release of <project_name>"``.

#. Push the changes: ``git push -u origin <project_name>``.

#. Visit https://github.com/conda-forge/staged-recipes and create a PR.

#. Read through the pre-filled text in the PR message and follow the instructions.

#. After the CI passes, create a new comment: ``@conda-forge/help-python Hello Team, ready for review!``.

.. _conda-forge-recipe-review:

Step 3. Wait for recipe review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Wait for a ``conda-forge`` volunteer reviewer to review your submission. It may take up to one week.

#. Once the PR is merged by the reviewer (1) your package is available on conda-forge, and (2) a new repository will be created under https://github.com/conda-forge/package-name-feedstock/. Example: https://github.com/conda-forge/diffpy.structure-feedstock.

#. After the PR is merged, the CI will automatically build the package and upload it to the conda-forge channel. You can check the status of the build by visiting ``https://anaconda.org/conda-forge/<package-name>.``

#. Done!

.. _conda-forge-feedstock-release:

How do I release a new version? I have the conda-forge feedstock
----------------------------------------------------------------

We release a new package once we have updated the ``version`` and ``SHA256`` sections in ``meta.yaml`` in ``https://github.com/conda-forge/<package-name>-feedstock`` on the ``main`` branch. The conda-forge team asks that you only modify ``meta.yaml``.

First, copy the ``SHA256`` value from `pypi.org <http://pypi.org>`_:

#. Visit the project on PyPI at ``https://pypi.org/project/<package-name>``

#. Click :guilabel:`Download files` under :guilabel:`Navigation`.

#. Click :guilabel:`view hashes` under :guilabel:`Source Distribution`.

#. Copy the :guilabel:`SHA256` value.

#. Create a PR to the feedstock repository.

#. If you haven't already, fork and clone the feedstock repository.

#. Run ``git checkout main && git pull upstream main`` to sync with the main branch.

#. Run ``git checkout -b <version-number>`` to create a new branch.

#. Open ``recipe/meta.yaml`` and modify the ``version`` and ``sha256``.

#. Run ``git add recipe/meta.yaml && git commit -m "release: ready for <version-number>"``.

#. Run ``git push --set-upstream origin <version-number>``.

#. Create a PR to ``upstream/main``.

#. Complete the relevant checklists generated in the PR comment.

#. Wait for the CI to pass and tag the relevant maintainer(s) for review.

#. Once the PR is merged, in 20 to 30 minutes, verify the latest conda-forge package version from the README badge or by visiting ``https://anaconda.org/conda-forge/<package-name>`` (e.g., ``https://anaconda.org/conda-forge/diffpy.utils``).

#. Done! Your package can now be installed using ``conda install <package-name>``.

.. seealso::

    For your next release, you can automate Steps 1 through 12 by running ``package update conda-forge`` in your command line. Read the section below :ref:`conda-forge-pr-automate`.

.. _conda-forge-pr-automate:

Can I automate the process of making a PR to the feedstock after PyPI/GitHub release?
----------------------------------------------------------------------------------------

Yes! We provide ``package update conda-forge`` to streamline the conda-forge release process after a PyPI release.

#. Open ``~/.skpkgrc``.

#. If you have not already, add ``feedstock_path`` where your cloned ``<package-name>-feedstock`` directories are located.

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
                "project_name": "<local-default-project-name>"
            },
            "feedstock_path": "<directory-path-containing-feedstocks>"
        }

    .. note:: What are the ``<local-default-...>`` values under ``default_context``? You can override the existing default prompts when a new package is created. For more, please read :ref:`faq-set-default-prompt-value`.

#. Save ``~/.skpkgrc``.

#. Type ``package update conda-forge``.

#. Enter the number corresponding to the package. It will create a PR from ``origin/<latest-version>`` to ``upstream/main``.

#. Done! Finish the rest of the steps provided in :ref:`conda-forge-feedstock-release`.



.. _conda-forge-pre-release:

Appendices
-----------

Appendix 1. How do I do pre-release?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generate ``meta.yaml`` by following ``Step 1`` and ``Step 2`` under ``conda-forge: release for the first time`` above. Here are two differences required for pre-release:

#. Create ``recipe/conda_build_config.yaml`` containing

    .. code-block:: yaml

      channel_targets:
         - conda-forge <package-name>_rc

#. In the ``version`` of ``meta.yaml``, enter ``<version>rc<rc-number>`` (e.g., enter ``0.0.3rc1`` instead of ``0.0.3-rc.1``). This is because PyPI uses the ``<version>rc<rc-number>`` format for pre-releases.

#. See an example here: https://github.com/conda-forge/diffpy.pdffit2-feedstock/blob/rc/recipe/conda_build_config.yaml

#. Make a PR into ``rc`` instead of ``main``.

#. Re-render once the PR is created.

#. To install your ``rc`` version, use the command:

    .. code-block:: bash

       conda install -c conda-forge/label/<package-name>_rc -c conda-forge <package-name>

For more, read the conda-forge official documentation for pre-release: https://conda-forge.org/docs/maintainer/knowledge_base/#pre-release-builds

.. _conda-forge-add-admin:

Appendix 2. Add a new admin to the conda-forge feedstock
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check whether you are an admin listed in the ``meta.yaml`` in the feedstock repository. Create an issue with the title/comment: ``@conda-forge-admin, please add user @username``. Please see an example issue `here <https://github.com/conda-forge/diffpy.pdffit2-feedstock/issues/21>`_.

.. _meta-yaml-info:

Appendix 3. Background info on ``meta.yml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``meta.yaml`` file contains information about dependencies, the package version, the license, the documentation link, and the maintainer(s) of the package. In ``meta.yaml``, there are 3 important keywords under the ``requirements`` section: ``build``, ``host``, and ``run`` that are used to specify dependencies.

    - ``build`` dependencies used for compiling but are not needed on the host where the package will be used. Examples include compilers, CMake, Make, pkg-config, etc.

    - ``host`` dependencies are required during the building of the package. Examples include setuptools, pip, etc.

    - ``run`` dependencies are required during runtime. Examples include matplotlib-base, numpy, etc.

To avoid any confusion, there is a separate YAML section called ``build`` above the ``requirements`` section. This section is for setting up the entire operating system. For more information, please refer to the official documentation: https://conda-forge.org/docs/maintainer/adding_pkgs/#build-host-and-run
