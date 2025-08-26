At the moment, the GitHub repository is empty. Let's create a local branch called ``main`` and upload this local branch to the remote GitHub repository.

#. Follow the series of steps to initialite ``Git``.  You only have to do this once.

    .. code-block:: bash

        git init
        git remote add origin <your-github-repo-url>
        git branch -M main

#. Commit the README file to the Git database and push it to the remote GitHub repository:

    .. code-block:: bash

        git add README.md   # If you are using Level 4
        git add README.rst  # If you are using Level 5
        git commit -m "docs: add README"
        git push -u origin main

    .. note:: What's ``origin``?

        ``origin`` is the default name for the remote repository under your GitHub account. You can think of it as a nickname for the remote repository. You can also use any other name you like, but ``origin`` is the most common convention. For more, please read :ref:`faq-github-terminology`.

    .. note:: What is ``-u`` next to ``git push``?

        The ``-u`` flag tells Git to set the upstream (remote) branch for the local branch. This means that in the future, you can simply use ``git push`` without specifying the remote and branch name, and Git will know where to push your changes.
