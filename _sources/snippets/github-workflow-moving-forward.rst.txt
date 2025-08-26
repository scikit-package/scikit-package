
Assume that you have successfully followed the previous steps. Now, you want to add new code to your GitHub repository. Perhaps you are working with a group of people. Here is a high-level overview with step-by-step instructions on how to do that:

#. Pull the latest code from the remote ``main`` branch:

    .. code-block:: bash

        git checkout main
        git pull origin main

    .. note::

        Recall that we used the name ``origin`` as the nickname for the remote GitHub repository.

#. Ensure that your local ``main`` branch is synced with the remote ``main`` branch by running:

    .. code-block:: bash

        git log

#. Create a new local branch from the ``main`` branch. Let's call this branch ``skpkg``:

    .. code-block:: bash

        git checkout -b <branch-name>

#. Modify any file that you want. Then, stage and commit the changes:

    .. code-block:: bash

        git add <file-modified-added-deleted>
        git commit -m "feat: <your commit message>"

#. Push your code from ``<branch-name>`` to the remote ``<branch-name>`` branch:

    .. code-block:: bash

        git push --set-upstream origin <branch-name>

#. Visit your GitHub repository.

#. Create a PR from ``origin/<branch-name>`` to ``origin/main``.

#. Wait for the ``Tests on PR`` and ``pre-commit`` checks to pass.

#. Merge the PR, delete the branch.

#. Repeat the steps in this section.

#. Done!
