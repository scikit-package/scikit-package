.. _codecov-token-setup:

We also want to ensure we report that tests are written for the incoming code and report in the incoming PR as shown below:

.. image:: ../img/codecov-pr.png
    :alt: codecov-in-pr-comment

.. warning::

    **Is this NOT your first time setting up Codecov?** Setting up the Codecov report can be done just once for all projects under your account or a GitHub organization with the "global token." Please check whether you already have a Codecov token. If it exists, you may still follow the steps, but you don't have to create a new token. Instead, you can use the existing token.

#. Ensure your GitHub repository is public.

#. Visit ``https://app.codecov.io/account/gh/<your_github_username_or_orgname>/org-upload-token``, replacing ``<your_github_username_or_orgname>`` with your actual GitHub username or organization name.

#. Under :guilabel:`Select an authentication option`, select ``Required``.

#. Click :guilabel:`Generate` or :guilabel:`Regenerate` to create a new token.

#. Click on the clipboard symbol to copy ``CODECOV_TOKEN``. Copy the one that starts with ``CODECOV_TOKEN=``. Here is an example of what it looks like:

    .. code-block:: text

        CODECOV_TOKEN=abcd1234-5678-1234-5678-b862619523bd

#. In your GitHub repository, visit :menuselection:`Settings --> Secrets and Variables --> Actions`.

#. If the repository is under your personal account, click :guilabel:`New repository secret`.

#. If the repository is under an organization, click :menuselection:`Manage organization secrets --> New organization secret`.

#. Under the :guilabel:`Name` field, type ``CODECOV_TOKEN``.

#. Under the :guilabel:`Secret` field, paste the ``CODECOV_TOKEN`` value you copied earlier without any modification.

#. Click :guilabel:`Add secret` to save the token.

#. Done. From now on, a new Codecov comment will be generated on each PR!
