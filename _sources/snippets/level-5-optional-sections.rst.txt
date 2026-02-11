Preview documentation in each pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Do you want to review documentation changes easily? Follow the instructions in :ref:`faq-doc-pr-preview` to view rendered documentation for each pull request with a public URL.

Build API reference documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/api-reference-doc.rst

Set up default prompt values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you create a new project in Level 3, 4 or 5, you will be prompted to enter the values for some variables, like ``maintainer_name``, ``maintainer_email`` and ``maintainer_github_username``. These variables have default values in the package. It can save your time and reduce errors if you can change the default values that are more relevant for your installation of ``scikit-package``.

To set up your own default promprt values, please refer to :ref:`faq-set-default-prompt-value`.

Update your level-5 packages without manual file migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tired of manually migrating files when updating your level-5 packages to the newest ``scikit-package`` standard? Try the ``package update`` command! It works like ``package create public``, but it automatically migrates your existing package files and removes placeholder files in the template.
