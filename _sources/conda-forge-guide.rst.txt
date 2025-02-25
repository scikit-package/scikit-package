:tocdepth: -1

==================================
How to release conda-forge package
==================================

.. _create-feedstock:

I already have a conda-forge feedstock. I want to release a new package version. How do I do that?
--------------------------------------------------------------------------------------------------

Please skip to :ref:`here <conda-forge-feedstock-release>`

I am new to conda-forge. How do I create a conda package?
---------------------------------------------------------

Here, you will learn how to release a conda package distributed through the conda-forge channel in 10 to 15 minutes. This guide assumes you are familiar with a basic clone, fork, and pull request workflow on GitHub.

Overview
^^^^^^^^

The process is divided into three steps:

1. :ref:`Prepare recipe: <conda-forge-recipe-prepare>` You will learn to prepare package information in a file called ``meta.yaml`` using our group's scikit-package template. The file serves as a recipe for building your conda package. The recipe contains the package version, the source code, the dependencies, the license, etc.

2. :ref:`Upload the recipe: <conda-forge-recipe-upload>` Once you have the ``meta.yaml`` generated, you will create a pull request the staged-recipe repository in the conda-forge repository `here <https://github.com/conda-forge/staged-recipes>`_

3. :ref:`Recipe review: <conda-forge-recipe-review>` One of the community members of conda-forge will review your ``meta.yaml`` and provide feedback. Once the recipe is approved, you will have a package available for ``conda install`` automatically, and you will have your own designated feedstock repository that contains ``meta.yaml`` in ``https://github.com/conda-forge/<package-name>-feedstock``.

.. _conda-forge-recipe-prepare:

1. Prepare conda package recipe in ``meta.yaml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To generate a package, we first need to generate a "recipe" for the package. The recipe contains the type of programming language, the package version, the source code, the dependencies, and license, etc. This recipe is stored in a file called ``meta.yaml``.

Hence, in Step 1, we will generate ``meta.yaml`` using the Billinge group's template. See https://github.com/conda-forge/diffpy.utils-feedstock/blob/main/recipe/meta.yaml as an example of a ``meta.yaml`` used in production.

If you are interested in learning more about each component within ``meta.yaml``, read :ref:`Appendix 1 <meta-yaml-info>` located at the end of this document.

1. Install ``scikit-package`` via ``pip install scikit-package`` and run ``package conda-forge``

2. Answer the following questions. Default values in parentheses are used if no value is provided.

 :github_org: The GitHub organization name. For example, ``diffpy``.

 :repo_name: The name of the repository.

 :module_name: The name of the module.

 :version: The version of the package.

 :source: Choose PyPI.

 :short_description: The short description of the project.

 :full_description: The full description of the project.

 :license_file: The license file that is located in your project repository. i.e., ``LICENSE.rst``.

 :maintainers: You may have multiple maintainers ``sbillinge, bobleesj`` or just ``sbillinge``.

 :build_requirements: copy ``requirements/build.txt`` from the project repo. It should be empty for pure Python packages.

 :host_requirements: Type ``python >=3.11, setuptools, setuptools-git-versioning >=2.0, pip`` from ``requirements/host.txt``.

 :runtime_requirements: Type the runtime dependencies from  ``requirements/conda.txt``.

 :testing_requirements: Type the testing dependencies from ``requirements/test.txt``.

Now, you have ``recipes/<package-name>/meta.yaml`` generated.

.. important::
   - For a pure python package, have you removed the ``build`` section under the ``requirements``? See https://github.com/conda-forge/diffpy.utils-feedstock/blob/main/recipe/meta.yaml for example.

   - Have you double-checked the license file name in ``meta.yaml`` against the license files in the project repository. If you are unsure, please confirm with the repository owner (Prof. Billinge).


.. _conda-forge-recipe-upload:

1. Upload ``meta.yaml`` to conda-forge for initial review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Fork https://github.com/conda-forge/staged-recipes and clone your forked repository

2. cd into ``staged-recipes``

3. Create ``recipes/<package-name>/meta.yaml`` Ex) ``recipes/diffpy.srreal/meta.yaml``

4. Copy and paste the content of ``meta.yaml`` from Step 1.

5. Create a new branch: ``git checkout -b <project_name>``

6. Add and commit the changes: ``git add . && git commit -m "Committing recipe for conda-forge release of <project_name>"``

7. Push the changes: ``git push -u origin <project_name>``

8. Visit https://github.com/conda-forge/staged-recipes and create a PR.

9. Read through the pre-filled text in the PR message and follow the instructions.

10. After the CI passes, create a new comment: ``@conda-forge/help-python Hello Team, ready for review!``

.. _conda-forge-recipe-review:

3. Wait for recipe review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Wait for a ``conda-forge`` volunteer reviewer to review your submission. It may take up to one week.

2. Once the PR is merged by the reviewer (1) your package is available on conda-forge, and (2) a new repository will be created under https://github.com/conda-forge/package-name-feedstock/. Example: https://github.com/conda-forge/diffpy.structure-feedstock.

.. _conda-forge-feedstock-release:

Use the conda-forge feedstock to release a new version
------------------------------------------------------

We release a new package once we have the ``version`` and ``SHA256`` sections in ``meta.yaml`` in ``https://github.com/conda-forge/<package-name>-feedstock`` located in the ``main`` branch. The conda-forge team asks to only modify ``meta.yaml``.

First, we will copy the ``SHA256`` value from `pypi.org <http://pypi.org>`_:

#. Visit the project on PyPI at ``https://pypi.org/project/<package-name>``

#. Click ``Download files`` under ``Navigation``

#. Click ``view hashes`` under ``Source Distribution``

#. Copy the ``SHA256`` value

#. Create a PR to the feedstock repository.

#. If you haven't, fork and clone the forked feedstock repository.

#. Run ``git checkout main && git pull upstream main`` to sync with the main branch.

#. Run ``git checkout -b <version-number>`` to create a new branch.

#. Open ``recipe/meta.yaml``, modify ``set version`` and ``sha256``.

#. Run ``git add recipe/meta.yaml && git commit -m "release: ready for <version-number>"``.

#. Run ``git push --set-upstream origin <version-number>``.

#. Create a PR to ``main``, complete the relevant checklists generated in the PR comment.

#. Wait for the CI to pass and tag Project Owner for review.

#. Once the PR is merged, in 20 to 30 minutes, verify the latest conda-forge package version from the README badge or by visiting ``https://anaconda.org/conda-forge/<package-name>``. i.e.g, ``https://anaconda.org/conda-forge/diffpy.utils``.


.. _conda-forge-pre-release:

Appendix 1. How do I do pre-release?
------------------------------------------------------------------------------

Generate ``meta.yaml`` by following ``Step 1`` and ``Step 2`` under ``conda-forge: release for the first time`` above. Here are two differences required for pre-release:

1. Create ``recipe/conda_build_config.yaml`` containing::

    channel_targets:
       - conda-forge <package-name>_rc

See an example here: https://github.com/conda-forge/diffpy.pdffit2-feedstock/blob/rc/recipe/conda_build_config.yaml

1. Make a PR into ``rc`` instead of ``main``. Re-render once the PR is created.

To install the pre-release build::

    conda install -c conda-forge/label/<package-name>_rc -c conda-forge <package-name>

For more, read the documentation for pre-release: https://conda-forge.org/docs/maintainer/knowledge_base/#pre-release-builds

Appendix 2. Add a new admin to the conda-forge feedstock
--------------------------------------------------------

Check whether you are an admin listed in the ``meta.yaml`` in the feedstock repository. Create an issue with the title/comment: ``@conda-forge-admin, please add user @username``. Please see an example issue `here <https://github.com/conda-forge/diffpy.pdffit2-feedstock/issues/21>`_.


.. _meta-yaml-info:

Appendix 3. Background info on ``meta.yml``
-------------------------------------------

The ``meta.yaml`` file contains information about dependencies, the package version, the license, the documentation link, and the maintainer(s) of the package. In ``meta.yaml``, there are 3 important keywords under the ``requirements`` section: ``build``, ``host``, and ``run`` that are used to specify dependencies.

- ``build`` dependencies used for compiling but are not needed on the host where the package will be used. Examples include compilers, CMake, Make, pkg-config, etc.

- ``host`` dependencies are required during the building of the package. Examples include setuptools, pip, etc.

- ``run`` dependencies are required during runtime. Examples include matplotlib-base, numpy, etc.

To avoid any confusion, there is a separate YAML section called ``build`` above the ``requirements`` section. This section is for setting up the entire operating system.

For more information, please refer to the official documentation: https://conda-forge.org/docs/maintainer/adding_pkgs/#build-host-and-run

.. _conda-forge-add-admin:
