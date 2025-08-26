.. _example-2:

Example 2. Create your first Level 5 public package
======================================================

In this example, we demonstrate how to create a new Level 5 public package from scratch. In this example the **maintainer** of the repository, who will have merge-rights, will be **Sir Lancelot**. To create the structure for the full featured public package he enters the following commands:

.. code-block:: bash

    $ cd ~/dev
    $ conda activate skpkg-env
    $ package create public

We show the responses of **Sir Lancelot** to the ``scikit-package`` prompts below. As described in Example 1, he followed group practice and located the empty project under ``∼/dev``. The text in parentheses are the default values supplied by ``scikit-package``. These can be user-configured but in the example we show the ``scikit-package`` defaults. Where there is no response **Sir Lancelot** simply hit the “Enter” key to accept the default value:

.. code-block:: bash

    [1/16] maintainer_name (Simon Billinge): Sir Lancelot
    [2/16] maintainer_email (sb2896@columbia.edu): sirlancelotbrave@montypy.com
    [3/16] maintainer_github_username (sbillinge): sirlancelotbrave
    [4/16] contributors (Sangjoon Lee, Simon Billinge, Billinge Group members):
        Sir Lancelot, Sir Robin, King Arthur
    [5/16] license_holders (The Trustees of Columbia University in the City of New
        York): The Knights of the Round Table
    [6/16] project_name (diffpy.my-project): montypy
    [7/16] github_username_or_orgname (diffpy): kot-roundtable
    [8/16] github_repo_name (montypy):
    [9/16] conda_pypi_package_dist_name (montypy):
    [10/16] package_dir_name (montypy):
    [11/16] project_short_description (Python package for doing science.): A
        Python package for the the Knights of the Round Table.
    [12/16] project_keywords (diffraction, PDF, X-ray, neutron): knights, castle, Monty, Python
    [13/16] minimum_supported_python_version (3.11):
    [14/16] maximum_supported_python_version (3.13):
    [15/16] Select project_needs_c_code_compiled
    1 - No
    2 - Yes
    Choose from [1/2] (1):
    [16/16] Select project_has_gui_tests
    1 - No
    2 - Yes
    Choose from [1/2] (1):

The questions are designed to be somewhat self-describing, but what they mean and how they are used is described in detail :ref:`level-5-tutorial`.

Given the answers to the questions in the example, **Sir Lancelot** sees the following folder structure created by ``scikit-package``:

.. code-block:: bash

    ~/dev
        |-- montypy
            |-- .codecov.yml
            |-- .codespell
                |-- ignore_lines.txt
                |-- ignore_words.txt
            |-- .flake8
            |-- .github
                |-- ISSUE_TEMPLATE
                    |-- bug_feature.md
                    |-- release_checklist.md
                |-- PULL_REQUEST_TEMPLATE
                    |-- pull_request_template.md
                |-- workflows
                    |-- build-wheel-release-upload.yml
                    |-- check-news-item.yml
                    |-- matrix-and-codecov-on-merge-to-main.yml
                    |-- publish-docs-on-release.yml
                    |-- tests-on-pr.yml
            |-- .gitignore
            |-- .isort.cfg
            |-- .pre-commit-config.yaml
            |-- .readthedocs.yaml
            |-- AUTHORS.rst
            |-- CHANGELOG.rst
            |-- CODE-OF-CONDUCT.rst
            |-- LICENSE.rst
            |-- MANIFEST.in
            |-- README.rst
            |-- docs
                |-- Makefile
                |-- make.bat
                |-- source
                    |-- _static
                        |-- .placeholder
                |--  api
                    |-- montypy.example_package.rst
                    |-- montypy.rst
                |--  conf.py
                |-- getting-started.rst
                |-- img
                    |-- scikit-package-logo-text.png
                |--  index.rst
                |-- license.rst
                |-- release.rst
                |-- snippets
                    |--  example-table.rst
            |-- news
                |-- TEMPLATE.rst
            |-- pyproject.toml
            |-- requirements
                |-- build.txt
                |-- conda.txt
                |-- pip.txt
                |-- tests.txt
                |-- docs.txt
            |-- src
                |-- montypy
                    |-- __init__.py
                    |-- functions.py
                    |-- version.py
            |-- tests
                |-- conftest.py
                |-- test_functions.py
                |-- test_version.py

After setting up the repository structure, **Sir Lancelot** adds code to the empty package by creating files in the ``./src/montpy`` directory. Any unit tests he adds in the tests directory. Previously written files can also be copied over from wherever they were on his hard drive, as in Example 1. Below we show the ``src`` and ``tests`` part of the directory tree after **Sir Lancelot** completed these steps:

.. code-block:: bash

    ~/dev
        |-- montypy
            |-- ...
            |-- src
                |-- montypy
                    |-- __init__.py
                    |-- utils.py
                    |-- grail
                        |-- __init__.py
                        |-- bridge_of_death.py
                        |-- black_knight.py
                    |-- version.py
            |-- tests
                |-- conftest.py
                |-- test_utils.py
                |-- test_bridge_of_death.py
                |-- test_black_knight.py

**Sir Lancelot** made some choices about the structure of his package by choosing the directory structure within ``.../src/montypy``. This affects what the importing syntax looks like and **Sir Lancelot** made the choices so his code will be more organized and readable. His choices resulted in import statements exemplified below,

.. code-block:: bash

    from montypy.utils import sword
    from montypy.grail.bridge_of_death import questions_three

assuming functions ``sword()`` and ``questions three()`` are defined in the modules ``utils.py`` and ``bridge_of_death.py``, respectively.

Once created, the package can be put under Git control and pushed to a repository with the name ``montypy`` that **Sir Lancelot** creates at GitHub, following the approach in Example 1. In the example, **Sir Lancelot** chose to create the new GitHub repository called **montypy**, under the **kot-roundtable** GitHub organization. The step-by-step tutorial for doing this is provided in :ref:`level-5-tutorial` In this example the code could then be found at https://github.com/kot-roundtable/montypy.

Recommended GitHub workflow for larger teams
--------------------------------------------

Unlike Example 1, we here introduce a forking workflow to maintain the package. The following workflow appears initially as somewhat complicated and unnecessarily pedantic, but for group coding, following these steps quickly pays huge dividends and is worth the extra up-front effort to set up and learn in a group setting.

In our example, let's assume that **Sir Lancelot** wants a new code feature under the ``grail`` sub-package. He first creates an issue on the GitHub repository where he clicks “New Issue” and selects the **“Bug Report / Feature Request”** template provided by ``scikit-package``. He sets the title to **feat: add bucket to utils**.

On the issue page, he describes the problem, “made a spill, need a bucket” and proposes a solution “implement a bucket in utils.py”. GitHub provides a number for the issue, for example #24, which will be used later.

In the issue title, **Sir Lancelot** added the prefix ``feat:``. Common prefixes like bug: and doc: are used in issue titles and commit messages to help track and organize them.

A contributor to the **kot-roundtable** org, **Sir Robin**, agreed to take the issue. **Sir Lancelot** and **Sir Robin** can discuss how to proceed in the comments thread of the issue, which results in a consensus to proceed. The issue can then be assigned by **Sir Lancelot** to **Sir Robin** so other contributors know it is under development.

In the forking workflow, **Sir Robin** will make a linked copy of the montypy repo under his own GitHub user namespace. This is called a Fork. He does this by visiting https://github.com/kot-roundtable/montypy and clicking the Fork button, which results in a new linked repository at https://github.com/sirrobinbrave/montypy.

**Sir Robin** then clones this fork to his local computer with these commands:

.. code-block:: bash

    $ cd ~/dev
    $ git clone https://github.com/sirrobinbrave/montypy.git
    $ cd montypy

On **Sir Robin**'s local computer he has a clone of the repository that is linked to his fork, but it doesn't automatically know that the fork is linked to a repository upstream of the fork in the **kot-roundtable** org. **Sir Robin** then runs this command to link his local repository to the upstream one:

.. code-block:: bash

    $ git remote add upstream https://github.com/kot-roundtable/montypy.git

**Sir Robin** can now keep his local repository synchronized with all changes that are merged into the upstream repository by typing the following command:

.. code-block:: bash

    $ git checkout main
    $ git pull upstream main

**Sir Robin** is then ready to check out a new branch to make some edits. He can give it any name but chooses one that he can recognize in the future:

.. code-block:: bash

    $ git checkout -b bucket

This bucket branch was branched from the current, most up-to-date, version of the main branch from the upstream GitHub repository under **kot-roundtable**. This maximizes the probability that his edits can be merged without conflict when they are done. Not remembering to create new branches from a fully synchronized upstream main is one of the most common errors we see for people new to the forking workflow.

The alias (name) for remote repositories can be anything, but by convention, and in our example, the repository called ``origin`` links to the remote repository under username ``sirrobinbrave`` and the one called ``upstream`` is linked to the remote repository in the **kot-roundtable** org.

We recommend a workflow where branches are very granular and only contain one, or a very few, features/fixes. This makes it much easier to merge branches and keep the development flowing. To the extent possible, we also recommend making branches independent of each other by creating each branch off the fully synchronized main branch. These are also common mistakes of people new to the forking workflow.

In **Sir Robin**'s branch he starts by defining a ``test_bucket()`` test function in test ``utils.py``, and defining an empty function ``def bucket()``: in the ``utils.py`` module. **Sir Robin** then stages and commits the changes using the commands below:

.. code-block:: bash

    $ git add tests
    $ git add src/montypy/
    $ git commit -m "feat: tests and function signature for bucket()"

We recommend that contributors share code with maintainers as early as possible in the process, allowing for rapid, early feedback. In the example, **Sir Robin** does this by creating a “Pull request”, or PR, on the upstream repository in order to solicit the feedback. To accomplish this **Sir Robin** first must push the new branch with the local changes to his GitHub repository:

.. code-block:: bash

    $ git push --set-upstream origin bucket

The ``--set-upstream`` modifier, which can be shortened to ``-u``, creates a permanent link between the local checked out branch (called ``bucket``) with a branch of the same name on **Sir Robin**'s fork, ``sirrobinbrave/montypy``. Then, finally, to create the PR **Sir Robin** uses his browser to visit the upstream repository (``kot-roundtable/montypy``) on GitHub and clicks the ”Pull Request” button. There are many other ways to create the PR including integrations in IDEs such as PyCharm or Visual Studio, using the GitHub Desktop GUI application or the GitHub CLI.

In the body of the top-level comment box of the pull request, **Sir Robin** typed instructions that he wanted the maintainer, **Sir Lancelot**, to know to help in the review. He also included the text, **closes #24**, where 24 is the issue number of **Sir Robin**'s bucket issue. Using this syntax tells GitHub to automatically close the linked issue when the pull request is approved and merged into the main branch. This is a very useful feature in GitHub.

This “PR” requests the maintainer of the upstream repository to “pull” the changes in branch bucket in **Sir Robin**'s fork into the main branch on the upstream repository. Before doing that, **Sir Lancelot** wants to ensure that everything is just so with the code and so provides a code review on GitHub giving feedback to **Sir Robin**. If there are multiple maintainers or contributors, others can also review the code and suggest improvements before the changes are merged.

Next, **Sir Robin** added a “news” file by copying ``news/TEMPLATE.rst`` to ``news/bucket.rst`` and editing it such that under the **Added** section he replaced ``<news-item>`` with Bucket in utils for cleaning up spills. Later, at the next release, this will appear in ``CHANGELOG.rst`` as follows:

.. code-block:: text

    0.1.0
    =====

    **Added: **

    * Bucket in utils for cleaning up spills

News items are mostly user-facing information so at each release users can see what has been added, fixed and so on, and can be written with this in mind.

**Sir Robin** then adds and commits the news file:

.. code-block:: bash

    $ git add news/meaning.rst
    $ git commit -m "chore: news"

We note that it is possible to tag a PR as being a draft to let the maintainer know that the PR is there for feedback but is not finished and not ready to be merged.

In our example the maintainer, **Sir Lancelot**, suggests some changes in the desired behavior of ``bucket()`` that will allow it to be generalized and more widely usable. He recognizes that bucket could be used for fetching water as well as cleaning spills. **Sir Lancelot** suggests that **Sir Robin** add a second test to capture this new behavior. **Sir Robin** makes these edits and can add them to the same PR simply committing them and then pushing the updated branch to his fork:

.. code-block:: bash

    $ git push

The updates automatically appear in the PR and **Sir Lancelot** is notified by GitHub of the updates and can further comment on them.

With the tests written and capturing the desired behavior for the function, **Sir Robin** can start coding up the ``bucket()`` function, running the tests by typing ``pytest``. This “test-forward” coding approach is called “test driven development” and often results in better designed and executed code because more thought is given to desired behavior before any coding is done on the function itself. It is rarely done by individual programmers and is therefore not intuitive to them, but we have found that in a group context, it is a very powerful approach.

**Sir Robin** keeps coding and running tests until the tests all pass, committing and pushing to the same PR at reasonable intervals (the commits can be more frequent than the pushes). If there is new functionality it is generally recommended to also update user documentation on the same PR to avoid forgetting it. Anything that comes up that it doesn't make sense to fix on this PR can be captured in a new issue.

Finally, **Sir Lancelot** and **Sir Robin** agree that everything about the edits are good, all the CI is passing at GitHub, at which point **Sir Lancelot** merges the PR into main on the upstream repository.

The final step is then for **Sir Robin** to synchronize his local main with the updated upstream main. All subsequent branches, built off a synchronized ``upstream/main``, will therefore include this new feature. Along with **Sir Robin**'s bucket feature, the synchronization will also fetch any edits that were merged from other contributors.

Because his edits are merged into main **Sir Robin** can now delete the bucket branch from his local computer with ``git branch -d bucket``.

**Sir Robin** followed best practice and wrote a good docstring in the function definition. As a result, when the ``scikit-package`` continuous integration (described below) builds the documentation, the API will be automatically documented with the new function and its docstring appearing in the online docs, another nice feature of ``scikit-package``.

Continuous Integration (CI): automated GitHub workflows
-------------------------------------------------------

When **Sir Robin** created the PR, several separate GitHub workflows were automatically triggered. These workflows are controlled by workflow files, located in the .github/workflows directory, that were created when **Sir Lancelot** started a new Level 5 project using ``scikit-package``. Here are the workflows that both **Sir Robin** and **Sir Lancelot** would see:

  #. The first CI workflow, Tests on PR, runs pytest on all the unit tests the user wrote in the project.
  #. The second CI workflow runs pre-commit to check the code quality similar to when pre-commit is run locally. To ensure that this CI test passes, get in the habit of running pre-commit locally before committing and installing pre-commit as a commit hook.
  #. The third CI workflow uses the Codecov app, which adds a comment to the PRsummarizing which lines of code are not covered by unit tests. This workflow checks every new line of code to see if it is covered by a test and fails if insufficient tests are provided for the new code in the PR.
  #. The fourth CI workflow checks for a news file in the PR and is there as a reminder for this important task.

These workflows will run on GitHub without charge for any open-source software repository that is public. GitHub provides some free CI credits for private repositories, and it is also possible to use CI through paid plans.

For future development through this PR workflow, **Sir Robin** always waits for all CI checks to complete, either passing (green) or failing (red). For any failing tests, **Sir Robin** makes local edits on the branch, then commits and pushes those changes. When a PR is merged into main, another CI workflow is triggered to ensure that the final version of the code is tested not only on Linux but also across multiple operating systems and all Python versions specified when the package was created using ``scikit-package``. To modify the behavior of the CI, a maintainer such as **Sir Robin** can modify relevant files in the ``.github/workflows`` directory, as described in :ref:`faq-github-actions`.

Public Package Release
----------------------

We describe here what happens when **King Arthur** the codeowner, and **Sir Lancelot** the maintainer, are ready to publish the ``montypy`` package online and share it with the wider community. The goal is to make the package installable via the ``conda install montypy`` or ``pip install montypy`` commands.

At this point, all pull requests and issues relevant to the release must be merged and closed. To facilitate this process **Sir Robin** created a new GitHub issue using the Release template provided by ``scikit-package``. This issue provides a complete checklist of tasks, including testing the code, reviewing the documentation, and closing any remaining issues or pull requests, that the developer should follow to ensure a successful release.

After the checklist items are completed by **Sir Robin**, **Sir Lancelot** proceeds with the release. **Sir Lancelot** begins by checking out the main branch and pulling the latest code from upstream/main, i.e.:

.. code-block:: bash

    $ cd ~/dev/montypy
    $ git checkout main
    $ git pull upstream main # Assume forking workflow

``scikit-package`` automates the rather complex process of running releases, attempting to minimize the overhead by using reasonable defaults (which can be modified). The release is triggered by the maintainer, who must have the required privileges on the GitHub repository, by simply creating a Git tag with a name with a particular pattern. The pattern is that the tag-name follows the the semantic versioning syntax.

Semantic versioning involves three numbers separated by two periods, where the three numbers indicate MAJOR, MINOR and PATCH release numbers. In this example, it is an initial release so **Sir Lancelot** chooses the lowest non-patch release number, ``0.1.0``:

.. code-block:: bash

    $ git tag 0.1.0
    $ git push upstream 0.1.0

The automated release, up to and including the step of submitting to PyPI, is triggered on the push.

We strongly recommend doing a less public pre-release, or release-candidate (rc) before each public release. The release can then be tested and any issues fixed before the community becomes aware of it. This release-candidate is a public release in the sense that the release is deployed to GitHub and to PyPI but is tagged as a pre-release. It can be pip installed but only by specifying the full version number and can only be found on PyPI and GitHub by some digging.

In our example, **Sir Lancelot** could make a pre-release of the 0.1.0 release by running,

.. code-block:: bash

    $ git tag 0.1.0-rc.0
    $ git push upstream 0.1.0-rc.0

with exactly this format (included dashes and dots).

The default release obtained by typing pip install montypy remains as the existing release, but the pre-release can be installed in a test environment by explicitly specifying the release number, ``pip install montypy==0.1.0-rc.0`` If needed, a second rc release with some problems fixed would be numbered ``0.1.0-rc.1``, and so on.

Whether it is a release-candidate or a full release, the GitHub tag pushed to the upstream repository triggers a series of GitHub workflows, including a check to verify whether the user executing the tag is authorized. When the package was created, **Sir Lancelot** entered sirlancelotbrave in response to the ``maintainer_github_username`` prompt. The ``maintainer_github_username`` specified person (this can be updated manually in the workflows) is the only GitHub user authorized to run this release workflow. Otherwise, the workflow will fail and the release process will not proceed. This ensures that only an authorized person can release the code. Once the workflow succeeds, it will then create a new pre-release/release on GitHub and publish the package to PyPI.

We recommend to also make packages available on conda-forge which can host not just python and has powerful methods for checking the dependency tree of all packages. For hints for how to do this please visit :ref:`release-pypi-github`.

After verifying the package is available and functional, **Sir Robin** who created the GitHub Release issue, can close it which then completes the release lifecycle for the version.
