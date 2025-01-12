:tocdepth: -1

==================================
How to release conda-forge package
==================================

.. _create-feedstock:

I am new to conda-forge. How do I create a conda package?
---------------------------------------------------------

Here, you will learn how to release a conda package distributed through the conda-forge channel in 10-15 minutes. This guide assumes you are familiar with a basic clone, fork, and pull request (PR) workflow on GitHub.

Step 1. Prepare ``meta.yaml``. See Appendix 1 to learn more about ``meta.yaml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To generate a package, we first need to generate a "recipe" for the package. The recipe contains the type of programming language, the package version, the source code, the dependencies, and license, etc. This recipe is stored in a file called ``meta.yaml``.

Hence, in Step 1, we will generate ``meta.yaml`` using the Billinge group's template. See https://github.com/conda-forge/diffpy.utils-feedstock/blob/main/recipe/meta.yaml as an example of a ``meta.yaml`` used in production.

If you are interested in learning more about each component within ``meta.yaml``, read :ref:`Appendix 1 <appendix1>` located at the end of this document.

1. Install ``scikit-package`` via ``pip install scikit-package`` and run ``scikit-package https://github.com/billingegroup/staged-recipes-cookiecutter``

2. Answer the following questions. Default values in parentheses are used if no value is provided.

    1. github_org (diffpy):

    2. module_name (diffpy.my_project): diffpy.srreal

    3. github_repo_name (diffpy.srreal):

    4. version (1.0.0): 1.3.1

    5. Select source 1 - PyPi or 2 - GitHub: 1

       1. Choose 1. Conda package can be built using PyPI's ``sdist`` containing requirements files, src/tests, and ``pyproject.toml``

    6. project_short_description (Python package for doing science.):

    7. project_full_description (This is a Python package for doing science.):

    8. license_file (LICENSE.rst):

    9.  recipe_maintainers (sbillinge,):

    10. build_requirements ():

        1.  copy ``requirements/build.txt`` from the project repo.

        2.  Empty for pure Python packages, otherwise compilers will be required.

    11. host_requirements (python >=3.11, setuptools, setuptools-git-versioning >=2.0, pip,):

        1.  copy ``requirements/host.txt``

    12. runtime_requirements (python >=3.11, numpy,):

        1.  copy ``requirements/conda.txt``

    13. testing_requirements (pip, pytest,):
        1.  copy ``requirements/test.txt``


Now, you have ``recipes/<package-name>/meta.yaml`` is generated.

- [ ] For a pure python package, have you removed the ``build`` section under the ``requirements``? See https://github.com/conda-forge/diffpy.utils-feedstock/blob/main/recipe/meta.yaml for example.

- [ ] Have you double-checked the license file name in ``meta.yaml`` against the license files in the project repository. If you are unsure, please confirm with the repository owner (Prof. Billinge).


Step 2. Upload ``meta.yaml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Step 3. Wait for review and merge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Wait for a ``conda-forge`` volunteer reviewer to review your submission. It may take up to one week.

2. Once the PR is merged by the reviewer (1) your package is available on conda-forge, and (2) a new repository will be created under https://github.com/conda-forge/package-name-feedstock/. Example: https://github.com/conda-forge/diffpy.structure-feedstock.


I already have a conda package. How do I distribute a new package version?
--------------------------------------------------------------------------

This step assumes there is a new version of Python package released to PyPI. We will use that PyPI source code to generate a new conda package.

Obtain the ``SHA256`` value from `pypi.org <http://pypi.org>`_:

1. Visit the project on PyPI at ``https://pypi.org/project/<package-name>``

2. Click ``Download files`` under ``Navigation``

3. Click ``view hashes`` under ``Source Distribution``

4. Copy the ``SHA256`` value

Create a PR to your conda-forge feedstock:

1. Fork the feedstock repository i.g. https://github.com/conda-forge/diffpy.utils-feedstock.

2. Clone the forked repository.

3. Run ``git checkout main && git pull upstream main`` to sync with the main branch.

4. Run ``git checkout -b <version-number>`` to create a new branch.

5. Open ``recipe/meta.yaml``, modify 1) ``set version`` and 2) ``sha256``.

6. Run ``git add recipe/meta.yaml && git commit -m "Release <version-number>"``.

7. Run ``git push --set-upstream origin <version-number>``.

8. Create a PR to ``main``, complete the relevant checklists generated in the PR comment, and modify ``meta.yaml`` as needed.

9. Wait for the CI to pass and tag Prof. Billinge for review.

10. Once the PR is merged, verify the latest conda-forge package version from the README badge.

.. _conda-pre-release:

I am familiar with the regular conda release process. How do I do pre-release?
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

.. _appendix1:

Appendix 1. Background info on ``meta.yml``
-------------------------------------------

The ``meta.yaml`` file contains information about dependencies, the package version, the license, the documentation link, and the maintainer(s) of the package. In ``meta.yaml``, there are 3 important keywords under the ``requirements`` section: ``build``, ``host``, and ``run`` that are used to specify dependencies.

- ``build`` dependencies used for compiling but are not needed on the host where the package will be used. Examples include compilers, CMake, Make, pkg-config, etc.

- ``host`` dependencies are required during the building of the package. Examples include setuptools, pip, etc.

- ``run`` dependencies are required during runtime. Examples include matplotlib-base, numpy, etc.

To avoid any confusion, there is a separate YAML section called ``build`` above the ``requirements`` section. This section is for setting up the entire operating system.

For more information, please refer to the official documentation: https://conda-forge.org/docs/maintainer/adding_pkgs/#build-host-and-run
