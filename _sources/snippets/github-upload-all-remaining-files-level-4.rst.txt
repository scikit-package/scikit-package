
While we previously uploaded the ``README`` file to the remote GitHub ``main`` repository, this is not a recommended workflow. We want to ensure that before any code is pushed to the ``main`` branch, the incoming code **formatted**, **tested**, and **reviewed**. We will try to automate these tasks as much as we can while creating a pull request (PR) to the ``main`` branch.

#. Just in case, pull the latest code from the remote ``main`` branch to your local ``main`` branch:

    .. code-block:: bash

        git checkout main
        git pull origin main

#. Checkout a new branch called ``skpkg-system`` from the ``main`` branch:

    .. code-block:: bash

        git checkout -b skpkg-system
        git add .
        git commit -m "skpkg: start a new project with skpkg"
        git push -u origin skpkg-system

#. Visit your GitHub repository online.

#. Click on the new green button that says ``Compare & pull request``.

#. The PR title can be ``skpkg: start a new project with skpkg template``.

#. The ``base`` branch should be ``main`` and the ``compare`` branch should be ``skpkg-system``.

#. Click on the ``Create pull request`` button.

#. Wait for ``Tests on PR`` to run and pass. It runs ``pytest`` on the incoming code in each pull request.

#. Also wait for ``pre-commit`` CI to run and pass.

    .. note:: Did ``pre-commit CI`` fail?

        If the pre-commit failed, you will need to first pull the new commit created by ``pre-commit CI`` before making any new edits locally. You can do this by running the following command:

        .. code-block:: bash

         git pull origin skpkg-system
         git add <file-modified-that-fixes-pre-commit-error>
         git commit -m "chore: <your commit message>"
         git push

#. Click :guilabel:`Files changed` in the PR to to review the new files added to the repository.

#. Once reviewed, click :guilabel:`Merge pull request`.

#. Delete the ``skpkg-system`` remote branch after merging.

#. Visit your GitHub repository and confirm that the ``main`` branch is updated.

#. Congratulations! You are done!
