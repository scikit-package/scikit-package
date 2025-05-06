.. _news-file-guide:

Why do I need a news file for each PR?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to write good ``CHANGELOG.rst`` for each release version. These news items are of interest to both developers and technical users looking for specific keywords.

We can streamline the process of writing ``CHANGELOG.rst`` for each release by compiling the news items from the ``news`` directory.

Here an example ``CHANGELOG.rst`` https://github.com/Billingegroup/scikit-package/blob/main/CHANGELOG.rst

How do I write good a news item?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Do not remove ``news/TEMPLATE.rst``. Make a copy called ``<branch-name>.rst``.
- Do not modify other section headers in the rst file. Replace ``* <news item>``
- Begin with "No news", "no news", or "no news added" for trivial changes with the following format:
- For consistency, start with a capital letter and a verb. End with a period. Ex) ``Add automatic linting of .md, .yml, .rst files via prettier hook in pre-commit.``
- If you do not need to write a news item, still write the following format so that the CI can pass while it's not later merged to the ``CHANGELOG.rst`` file.

    .. code-block:: text

        **Added:**

        * No news: <brief reason>

Where to place the news item in ``<branch-name>.rst``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``**Added:**`` includes features or functionality of interest to users and developers, such as support for a new Python version or the addition of a useful feature.
- ``**Changed:**`` includes modifications that affect end-users or developers, such as API changes or dependencies replaced.
- ``**Fixed:**`` includes bug fixes or refactoring.
- ``**Deprecated:**`` includes methods, classes, or workflows that are no longer supported in the future release.
- ``**Removed:**`` includes the opposite of the "Added" section, referring to features or functionality that have been removed.
- ``Security:**``: include fixes or improvements related to vulnerabilities, authentication, or access control.
