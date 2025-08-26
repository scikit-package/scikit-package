Before we upload anything to the ``main`` branch, we want to check the incoming code **formatted**, **tested**, and **reviewed**. We will try to automate these tasks as much as we can while creating a pull request (PR) to the ``main`` branch.

#. Just in case, pull the latest code from the remote ``main`` branch to your local ``main`` branch:

    .. code-block:: bash

        git checkout main
        git pull origin main

#. Setup pre-commit locally so that code is linted before a commit is made:

    .. code-block:: bash

        pre-commit install

#. Checkout a new branch called ``skpkg-public`` from the ``main`` branch:

    .. code-block:: bash

        git checkout -b skpkg-public
        git add .
        git commit -m "skpkg: start a new level 5 project with skpkg"
        git push -u origin skpkg-public

    .. note::

        Did you see any failed ``pre-commit`` hooks after you typed ``git commit -m``? If so, no commit will be made. Confirm by typing ``git log``. Then, simply re-run ``git add <file>`` on the files that have been modified by ``pre-commit`` and re-enter the same commit message again, such as ``git commit -m "skpkg: start a new project with skpkg template"``. If you are having trouble getting a commit to be accepted, please refer to the FAQ section :ref:`faq-pre-commit-error`.
