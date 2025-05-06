.. _codecov-token-setup:

For each PR, we use ``Codecov`` to report the test coverage percentage change as shown below.

.. image:: ../img/codecov-pr.png
   :alt: codecov-in-pr-comment

To do so, the repository maintainer needs to provide a ``CODECOV_TOKEN``.  Please follow the step-by-step guide below.

#. Ensure your GitHub repository is public.

#. Visit https://app.codecov.io/

#. Connect your repository or organization with Codecov by clicking ``Configure Codecov's GitHub app``, shown below:

    .. image:: ../img/codecov-configure.png
        :alt: codecov-configure-github-project-button

#. Scroll down, find your repository of interest, and click ``Configure``, shown below:

    .. image:: ../img/codecov-projects.png
        :alt: codecov-list-github-projects

#. Scroll down again, copy ``CODECOV_TOKEN``, shown below:

    .. image:: ../img/codecov-token.png
        :alt: codecov-list-github-projects

#. In your GitHub repository, go to ``Settings``, then click ``Actions`` under the ``Secrets and Variables`` tab.

#. Click ``New repository secret``.

#. Paste the token value and name it as ``CODECOV_TOKEN`` secret as shown below:

    .. image:: ../img/codecov-github.png
        :alt: codecov-list-github-projects

#. Done. The **Codecov token** is now set up for the repository. From now on, a new comment will be generated on each PR with the Codecov status automatically.
