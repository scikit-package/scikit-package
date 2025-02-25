.. _news-file-guide:

We require that each PR includes a news item of ``<branch-name>.rst`` file under the ``news`` directory.

Motivation
""""""""""

``.rst`` files under the ``news`` directory are used to compile and update the ``CHANGELOG.rst`` file during releases. Hence, these news items are of interest to both developers and technical users looking for specific keywords.

Guidelines for writing news items
"""""""""""""""""""""""""""""""""

- Do not remove ``news/TEMPLATE.rst``. Make a copy called ``<branch-name>.rst``.
- Do not modify other section headers in the rst file. Replace ``* <news item>`` only. See example news files in `Example 1 <https://github.com/bobleesj/diffpy.utils/blob/ba4b985df971440325442a50ac6de63eaad05fa5/news/no-empty-object.rst>`_ and `Example 2 <https://github.com/bobleesj/diffpy.utils/blob/f79e88eadfcd7b58e84c6caa591a960d79689ba9/news/prettier-pre-commit.rst>`_.
- Begin with "No news", "no news", or "no news added" for trivial changes with the following format:

.. code-block:: text

    **Added:**

    * No news: <brief reason>

Where to place the news item in ``<branch-name>.rst``?
""""""""""""""""""""""""""""""""""""""""""""""""""""""

- ``**Added:**`` includes features or functionality of interest to users and developers, such as support for a new Python version or the addition of a useful feature.
- ``**Changed:**`` includes modifications that affect end-users or developers, such as API changes or dependencies replaced.
- ``**Fixed:**`` includes bug fixes or refactoring.
- ``**Deprecated:**`` includes methods, classes, or workflows that are no longer supported in the future release.
- ``**Removed:**`` includes the opposite of the "Added" section, referring to features or functionality that have been removed.

.. _codecov-token-setup:
