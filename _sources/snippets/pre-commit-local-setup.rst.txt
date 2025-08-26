First, let's ensure that before we upload any of our code to the remote repository, we lint the code and ensure that it is formatted correctly. We will use a library called ``pre-commit`` to do this.

#. Configure ``pre-commit`` to run each time a new commit is made. You only have to do this once. We assume you have pre-commit installed in your environment by running ``conda install pre-commit``:

    .. code-block:: bash

        pre-commit install

#. Let's now stage and commit the code:

    .. code-block:: bash

        git add .
        git commit -m "skpkg: initial commit of a new project"

#. Ensure that all of the ``pre-commit`` hooks pass:

    .. code-block:: text

        black....................................................................Passed
        prettier.................................................................Passed
        docformatter.............................................................Passed

    .. note::

        ``black`` is a tool that automatically formats Python code to conform to the PEP 8 style guide. ``prettier`` is a tool that formats code in various languages, including ``.md``, ``.rst``, and ``.json`` files. ``docformatter`` is a tool that formats docstrings in Python code.

#. You will see the new commit in the git log:

    .. code-block:: bash

        git log

    .. note::

        Did you see any failed ``pre-commit`` hooks? If so, no commit will be made. Simply re-run ``git add <file>`` on the files that have been modified by ``pre-commit`` and re-enter the same commit message again, such as ``git commit -m "skpkg: start a new project with skpkg template"``. If you are having trouble getting a commit to be accepted, please refer to the FAQ section :ref:`here<faq-pre-commit-error>`.
