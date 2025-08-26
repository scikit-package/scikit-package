Why do I need a news file for each PR?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to write a good ``CHANGELOG.rst`` for each release version. These news items are of interest to both developers and technical users looking for specific keywords. We can streamline the process of writing ``CHANGELOG.rst`` for each release by compiling the news items from the ``news`` directory.

Here is an example ``CHANGELOG.rst``: https://github.com/scikit-package/scikit-package/blob/main/CHANGELOG.rst

How do I create a news file?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In your repository, confirm that the ``news/TEMPLATE.rst`` file exists.

#. Make a copy of ``news/TEMPLATE.rst`` and name it ``news/<branch-name>.rst``. You can automate the process of creating the news file and adding new items by running the commands:

    .. code-block:: bash

        package add news --add -m "<Describe the main feature added in the PR.>"

    .. note::

        As shown above, you may use ``-a`` or ``--add``. The second flag, ``-m``, stands for ``message``.

#. Confirm that your ``news/<branch-name>.rst`` has the following content:

    .. code-block:: text

        **Added:**

        * <Describe the main feature added in the PR.>

        **Changed:**

        * <news item>

        **Deprecated:**

        * <news item>

        **Removed:**

        * <news item>

        **Fixed:**

        * <news item>

        **Security:**

        * <news item>

    .. seealso::

        Once you are happy with the news item(s) that you have added, you don't need to modify anything in ``news/<branch-name>.rst`` or ``news/TEMPLATE.rst``. ``scikit-package`` will automatically parse your news items and add them to the ``CHANGELOG.rst`` file when you initiate a release.

    .. note::

        Although it is generally not recommended, if two tasks were completed on the same branch, you can still add another news item by running the ``package add news`` command again.

Where do I place my news item in ``<branch-name>.rst``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``**Added:**`` (``-a``, ``--add``) includes features or functionality of interest to users and developers, such as support for a new Python version or the addition of a useful feature.
- ``**Changed:**`` (``-c``, ``--change``) includes modifications that affect end users or developers, such as API changes or replaced dependencies.
- ``**Fixed:**`` (``-f``, ``--fix``) includes bug fixes or refactoring.
- ``**Deprecated:**`` (``-d``, ``--deprecated``) includes methods, classes, or workflows that will no longer be supported in a future release.
- ``**Removed:**`` (``-r``, ``--remove``) is the opposite of the "Added" section, referring to features or functionality that have been removed.
- ``**Security:**`` (``-s``, ``--security``) includes fixes or improvements related to vulnerabilities, authentication, or access control.

What are good practices for writing news items?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Maintain consistency when a new release note is created and added to the ``CHANGELOG.rst`` file:

    a. Start with an active verb.
    b. Capitalize the first word.
    c. End with a period.
    d. Use the ``rst`` style of backquotes instead of the markdown style. For example, use ````scikit-package```` instead of ```scikit-package```.

    e.g., Add automatic linting of ``.md``, ``.yml``, and ``.rst`` files via a prettier hook in pre-commit.

My PR has trivial fixes that shouldn't be in ``CHANGELOG.rst``. Should I still create a news file?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. In this case, we want to communicate to the reviewer(s) the reason it should not be in the ``CHANGELOG.rst``. You can simply run the following:

    .. code-block:: bash

        package add news -n -m "<brief-reason>."

You will see a new file has been created: ``news/<branch-name>.rst``

    .. code-block:: text

        **Added:**

        * No news: <brief-reason>

        ...
