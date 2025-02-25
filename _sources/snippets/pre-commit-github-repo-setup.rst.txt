.. _pre-commit-github-repo-setup:

Appendix 5. How to configure pre-commit CI via GitHub Apps
----------------------------------------------------------

``Pre-commit CI`` is available as a GitHub app that executes pre-commit hooks in each pull request, as shown in the image below. While it is recommended to run ``precommit run --all-files`` locally before making a PR, this GitHub app will automatically attempt to lint code and format docstrings according to the hooks provided in ``.pre-commit-config.yaml``. If all passes, it will give you a green checkmark as shown below.

.. image:: ./img/precommit-PR.png
   :alt: pre-commit-PR-automatic-check

To configure ``pre-commit CI``, follow the simple steps below:

#. Visit https://github.com/apps/pre-commit-ci and click "Configure".

#. Select the repository(s).

#. Done!
