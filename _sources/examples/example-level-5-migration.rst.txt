.. _example-4:

Example 4. Migrate an existing package to Level 5
=================================================

In the final example, we demonstrate how you can migrate an existing legacy Python package to the Level 5 public standard. As in :ref:`example-2`, we adopt the forking GitHub workflow where **Sir Lancelot** is the maintainer and **Sir Robin** is the contributor**. The migration process is divided into two parts. The first involves fixing legacy issues that allow the existing code to pass pre-commit. Second, a new package directory structure is created and files from the old package are migrated over into the new package directory tree. The files fall into three categories, whether they are present just in the new package, just in the old package or in both. scikit-package has instructions for how to use Git to help with this transition.

Here we assume the legacy project is called ``flying-circus`` and it exists on GitHub under the ``kot-roundtable`` organization. In the past, **Sir Robin** has forked the ``flying-circus`` remote repository and cloned it onto his local computer in the ``∼/somewhere/on/my/computer`` folder using the forking workflow that was described in Example 2. As a result, **Sir Robin**'s file system has the following structure:

.. code-block:: bash

    ~/somewhere/
        |-- on/
            |-- my/
                |-- computer/
                    |-- flying-circus
                        |-- .gitignore
                        |-- .git/
                        |-- README.md
                        |-- setup.py
                        |-- requirements.txt
                        |-- flying_circus
                            |-- __init__.py
                            |-- surreal.py
                            |-- tests
                                |-- test_surreal.py

It is a legitimate package that has been released to the public, but it is not to the ``scikit-package`` Level 5 standards. For example, it uses the not-recommended ``setup.py`` rather than the preferred ``pyproject.toml`` to handle the package build.

Lint code with black
--------------------

The first step of bring it to standard involves autolinting the existing code with ``black`` to ``scikit-package`` syntax standards. As usual, **Sir Robin** starts by making sure his local repository is properly synchronized, then creates a new branch called ``black-edits`` for this work:

.. code-block:: bash

    $ cd ~/somewhere/on/my/computer/flying-circus
    $ git checkout main
    $ git pull upstream main
    $ git checkout -b black-edits

He then activates the ``skpkg-env`` Conda environment for doing the work and installs ``black``:

.. code-block:: bash

    $ conda activate skpkg-env
    $ conda install black

The configuration information for the black tool is held in a ``pyproject.toml`` file at the top level of the repository. Because **Sir Robin** doesn't have a ``pyproject.toml`` file, he will need to create one with the desired configuration. Following the ``scikit-package`` instructions,
he creates a ``pyproject.toml`` file (using ``touch pyproject.toml``) and adds this code block:

.. code-block:: text

    [tool.black]
    line-length = 79
    include = '\.pyi?$'
    exclude = '''
    /(
    \.git
    | \.hg
    | \.mypy_cache
    IUCr macros version 2.1.17: 2023/10/19
    45
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

If he wants he can modify the configuration to conform to the standards of the project he is working on, but for **flying-circus** he is happy to take the ``scikit-package`` defaults.

To run the auto-linter on the code, **Sir Robin** types the command ``black .``, where the dot means current directory and all subdirectories. This makes (generally) safe, automatic updates to all the code files it finds in the project. He can then commit the changes and make a PR so that **Sir Lancelot**, the project maintainer, can review and merge. He is careful not to make any manual edits in this PR so he tells **Sir Lancelot** that all the edits are from black, which makes it easy for **Sir Lancelot** to merge it.

Setup pre-commit to format code
-------------------------------

Next we continue with more linting activities beyond autolinting so that all the checks in pre-commit pass. At this point, following the ``scikit-package`` instructions, **Sir Robin** creates an empty Level 5 public project in the current directory by typing the following:

.. code-block:: bash

    $ cd ~/somewhere/on/my/computer/flying-circus  # he should already be here
    $ conda activate skpkg-env
    $ package create public

He answers the questions as in Example 2, giving ``flying-circus`` as the package name. This results in a new subdirectory in ``flying-circus`` called ``flying-circus`` (the same name). The steps are a bit involved and are discussed in detail in the ``scikit-package`` documentation. His directory structure now looks like the following:

.. code-block:: bash

    somewhere/
        |-- on/
            |-- my/
                |-- computer/
                    |-- flying-circus
                        |-- .gitignore
                        |-- .git/
                        |-- pyproject.toml
                        |-- README.md
                        |-- setup.py
                        |-- requirements.txt
                        |-- flying_circus
                            |-- __init__.py
                            |-- surreal.py
                            |-- tests
                                |-- test_surreal.py
                        |-- flying-circus  # Level 5 empty folder
                            |-- .codecov.yml
                            |-- .codespell
                                |-- ignore_lines.txt
                                |-- ignore_words.txt
                            |-- .flake8
                            |-- .github/
                            |-- .gitignore
                            |-- .isort.cfg
                            |-- .pre-commit-config.yaml
                            |-- .readthedocs.yaml
                            |-- src/
                            |-- tests/
                            |-- requirements/
                            |-- pyproject.toml
                            |-- ...

To begin with we need to take the ``pre-commit`` configuration files from the new package created by ``scikit-package`` and place them in the old package. These include the ``.pre-commit-config.yaml``, ``.isort.cfg``, ``.flake8``, and so on. After doing this, **Sir Robin**'s directory structure looks like this:

.. code-block:: bash

    somewhere/
        |-- on/
            |-- my/
                |-- computer/
                    |-- flying-circus
                        |-- .codespell
                            |-- ignore_lines.txt
                            |-- ignore_words.txt
                        |-- .flake8
                        |-- .isort.cfg
                        |-- .pre-commit-config.yaml
                        |-- .gitignore
                        |-- .git/
                        |-- pyproject.toml
                        |-- README.md
                        |-- setup.py
                        |-- requirements.txt
                        |-- flying_circus
                            |-- __init__.py
                            |-- surreal.py
                            |-- tests
                                |-- test_surreal.py
                        |-- flying-circus  # Level 5 empty folder
                            |-- .codecov.yml
                            |-- .codespell
                                |-- ignore_lines.txt
                                |-- ignore_words.txt
                            |-- .flake8
                            |-- .github/
                            |-- .gitignore
                            |-- .isort.cfg
                            |-- .pre-commit-config.yaml
                            |-- .readthedocs.yaml
                            |-- .gitignore
                            |-- src/
                            |-- tests/
                            |-- requirements/
                            |-- pyproject.toml
                            |-- ...

With this done, Sir Robin installs ``pre-commit`` in his environment and then runs it with this command:

.. code-block:: bash

    $ pre-commit run --all-files

He sees many errors raised by ``pre-commit``. He will fix them and get the cleaned code reviewed and merged by **Sir Lancelot** on a bunch of different branches and PRs, but to avoid these changes inadvertently breaking the code at the upstream repository, **Sir Lancelot** creates a new branch on the ``kot-roundtable/flying-circus`` repository at GitHub, calling it migration. All PRs that **Sir Robin** creates now he will request to have them merged into the migration branch, which he will use the same way he was using ``upstream/main``, keeping it synchronized and building new branches off the his local migration branch that is synchronized with ``upstream/migration``. Only at the end, when everything tested and working, will **Sir Lancelot** merge ``flying-circus/migration`` into ``flying-circus/main``.

**Sir Robin** continues his work to fix errors raised by ``pre-commit``. For each category of errors, **Sir Robin** creates a dedicated branch, grouping similar fixes together, with the commands,

.. code-block:: bash

    $ git checkout migration
    $ git pull upstream migration
    $ git checkout -b pre-commit-<theme>


For example, a branch called ``pre-commit-spelling`` contained spelling fixes, while another branch, ``pre-commit-flake8-line`` contained fixes of line length errors raised by ``flake8``. These were pushed to **Sir Robin**'s fork and PRs created into ``flying-circus/migration`` branch for review and merge by **Sir Lancelot**, as we have described. More granular branches make **Sir Lancelot**'s job to review and merge changes much easier.

Setup local CI after migrating essential files
----------------------------------------------

 With the package now passing all ``pre-commit`` checks and local tests, it is time to start migrating it to the new package structure created by ``scikit-package``. We do this by copying files from the old package into the directory structure created by ``scikit-package``.

 The old package was under git control. We have found that the best way to do the migration is to first move the Git database from the existing project directory to the new Level 5 package. This retains the entire git history of the old project, but places it in the new package structure created by ``scikit-package``. After we do this, the git controlled ``flying-circus`` package is now the new package and the files in the old package are no longer under git control, until we move them over.

  To move the Git database over, **Sir Robin** executes the below commands:

.. code-block:: bash

    $ cd flying-circus  # Enter Level 5 directory
    $ mv ../.git .      # Move Git database from old to new directory

When **Sir Robin** types ``git status``, he sees files listed as **deleted**, **added**, and **modified**. This is from the point of view of the Git database rather than actual reality.

    #. **deleted**: These are files that exist in the Git database but are no longer present in the new package structure (e.g. project source code).

    #. **Untracked files**: These are files that Git finds in the new package structure that do not yet exist in the Git database (i.e. new files introduced by ``scikit-package``).

    #. **modified**: These files exist in both the Git database and the new package structure, but their contents differ.

    #. (not listed): Files that exist in both locations and are identical will not appear in the git status output. As an example, the code in the old package (``surreal.py`` and ``test_surreal.py``) hasn't been moved over so will show in the list as deleted. The requirements and src directory trees don't exist in the old package and will be listed as untracked. pyproject.toml is in both places but with different content, so will show as modified. And, assuming that **Sir Robin** didn't modify any of the flake8 defaults, the .flake8 will not appear in the list at all as, from the point of view of the git database, it has not changed.

**Sir Robin** can then start the work of removing all the issues from the ``git status`` list bit by bit. He first copies over the code files with,

.. code-block:: bash

    $ cp -n ../flying_circus/surreal.py ./src/flying_circus/
    $ cp -n ../flying_circus/tests/test_surreal.py ./tests

The ``-n`` modifier in the cp command stands for “no clobber” and ensures that, if there is a file in the destination of the same name, the cp command will fail and the destination file will not be overwritten. Clearly this is not needed here, but it does no harm, and is a good habit to avoid errors in this migration process. When copying over entire directories, you would use the command ``cp -n -r`` where the ``-r`` means recursively and the copy command will copy all the subdirectories and their contents. Here the ``-n`` can be very important. However, pay attention to outputs from the cp command and make notes of any clashes that need to be manually resolved.

After the code is moved over, it should be possible to build the code in the new package and have the tests pass. **Sir Robin** updates the files in the requirements directory, ``docs.txt``, ``conda.txt``, ``pip.txt``, and ``tests.txt``, adding any dependencies that are needed for the code to run. **Sir Robin** can then confirm everything works with the code in the new package by creating a new environment and running the tests with the following commands:

.. code-block:: bash

    $ conda create -n flying-circus-env python=3.13
    $ conda install --file requirements/conda.txt
    $ conda install --file requirements/tests.txt
    $ pip install -e . --no-deps
    $ pytest

These changes can be committed, pushed and turned into a PR into the ``upstream/migration`` branch. Now, the tests are passing locally, but for them to pass in the CI on GitHub some more files need to be added to the Git database. In particular, add and commit the ``.github``directory, as well as the ``src/``, ``tests/``, and ``requirements/``, directories. If these are added to the PR, the unit tests should now also pass in the CI.

After the GitHub automated workflows pass, **Sir Lancelot** can review and merge th**e ``sirrobinbrave/setup-CI`` branch to the ``upstream/migration`` branch. **Sir Robin** can now move handwritten documentation files, such as tutorials under the doc directory and the ``README``. First, **Sir Robin** synchronizes his local ``migration`` branch and creates a new branch called doc.

Files that show as ``updated`` need to be handled carefully. They exist in the old package and the new package but with different contents and need to be manually merged by **Sir Robin**.

Some other files also need careful merging when they contain similar content but have a different name between the packages. For example, in this case the ``README.md`` file in the old package is renamed to ``README.rst`` in the new one. ``README.md`` therefore shows up as deleted and ``README.rst`` as untracked in the git status list. In this case **Sir Robin** will add and commit ``README.rst`` but then open them both in a text editor and copy any text over from the old ``README.md`` to the new ``README.rst``, before finally removing the ``README.md`` from the Git database using ``git rm README.md``. In this example, setup.py receives a similar treatment as its functionality is replaced by ``pyproject.toml`` in the new project, though some of the information in the old ``setup.py`` may still be needed in the new ``pyproject.toml`` and so is manually merged in an editor/IDE by **Sir Robin**.

The work is considered finished when:

    #. All files showing as ``deleted`` that need to be preserved have been moved from the old to the new structure directory structure.
    #. All files showing as ``deleted`` that are unwanted in the new package have been removed from the Git database using ``git rm <filename>``.
    #. All untracked files created by ``scikit-package`` have been git added and git committed.
    #. All modified files that exist in both the old and new locations have been reviewed and the contents merged.
    #. All resulting pull requests have been reviewed and merged by **Sir Lancelot**.

Finally, assuming all tests are passing and he is happy, **Sir Lancelot**, can merge the ``upstream/migration`` branch into the ``upstream/main`` default branch. In his computer, **Sir Robin** can then clean and organize things. He updates his local main from ``upstream/main`` and moves the new Level 5 package directory to his global ``dev`` folder using,

.. code-block:: bash

    # Move Level 5 directory to ~/dev
    $ mv somewhere/on/my/computer/flying-circus/flying-circus ~/dev

As a result **Sir Robin** sees that his package has been moved to the appropriate place with
all his code, resulting in the directory structure,

.. code-block:: bash

    ~dev/
        |-- flying-circus
            |-- .codecov.yml
            |-- .codespell/
            |-- .flake8
            |-- .github/
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
            |-- docs/
            |-- news/
            |-- pyproject.toml
            |-- requirements/
            |-- src
                |-- flying_circus
                    |-- __init__.py
                    |-- surreal.py
            |-- tests
                |-- test_surreal.py

and he is ready to continue to maintain and develop ``flying-circus`` as a community open source project.
