Why do I need a news file for each PR?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to write good ``CHANGELOG.rst`` for each release version. These news items are of interest to both developers and technical users looking for specific keywords.

We can streamline the process of writing ``CHANGELOG.rst`` for each release by compiling the news items from the ``news`` directory.

Here is an example ``CHANGELOG.rst`` https://github.com/scikit-package/scikit-package/blob/main/CHANGELOG.rst

How do I write good a news item?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Do not remove ``news/TEMPLATE.rst``. Make a copy called ``<branch-name>.rst``.
- Do not modify other section headers in the rst file. Replace ``* <news item>`` only.
- Start with a capital letter and a verb. End with a period, e.g., ``Add automatic linting of .md, .yml, .rst files via a prettier hook in pre-commit.``
- For trivial changes, still create ``<branch-name>.rst``, but the news item should start with ``* No news:`` so that the news item is not compiled into the ``CHANGELOG.rst`` file during the release process. Here is an example below:

    .. code-block:: text

        **Added:**

        * No news: <brief reason>

- Use the ``rst`` style of backquotes instead of the markdown style of backquotes. For example, use ````scikit-package```` instead of ```scikit-package```.

Where to place the news item in ``<branch-name>.rst``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``**Added:**`` includes features or functionality of interest to users and developers, such as support for a new Python version or the addition of a useful feature.
- ``**Changed:**`` includes modifications that affect end-users or developers, such as API changes or dependencies replaced.
- ``**Fixed:**`` includes bug fixes or refactoring.
- ``**Deprecated:**`` includes methods, classes, or workflows that are no longer supported in the future release.
- ``**Removed:**`` includes the opposite of the "Added" section, referring to features or functionality that have been removed.
- ``Security:**``: include fixes or improvements related to vulnerabilities, authentication, or access control.
