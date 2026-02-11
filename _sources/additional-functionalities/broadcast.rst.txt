.. _package_broadcast:

Broadcast a GitHub issue to multiple repositories with ``scikit-package``
=========================================================================

Overview
--------

This is a tutorial for using ``scikit-package`` to broadcast a GitHub issue to multiple repositories by running the command

    .. code-block:: bash

     package broadcast <issue-url> <group-name>

The command needs Github Personal Access Token and configuration files to work properly. Please see the following sections for more information.

Setup GitHub Personal Access Token
----------------------------------

Create a GitHub Personal Access Token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For detailed information, please check `GitHub documentation <https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token>`_.

#. Visit `Create GitHub Personal Access Tokens <https://github.com/settings/personal-access-tokens/new>`_.
#. Enter the ``Token name``. You may use  ``scikit-package`` or any other name you like.
#. Choose the ``Expiration`` date.
#. Select the scope of ``Repository access``.
#. Click the :guilabel:`Generate token` green button to create the token.
#. Copy the generated token into a safe place.

Add the token as an environment variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For Windows Users
~~~~~~~~~~~~~~~~~

#. Press ``Win + R`` and type ``sysdm.cpl`` or ``SystemPropertiesAdvanced``. Either command works.
#. Click the :guilabel:`Environment Variables...` tab in the :guilabel:`Advanced` tab.
#. Under the :guilabel:`User variables` section, click the :guilabel:`New...` button.
#. Set the :guilabel:`Variable name` to ``GITHUB_TOKEN``.
#. Set the :guilabel:`Variable value` to the GitHub Personal Access Token you created in previous section.
#. Click :guilabel:`OK` to save the new environment variable.
#. Done!

For Linux Users
~~~~~~~~~~~~~~~

#. Open the terminal profile, e.g., ``.bashrc``, ``.zshrc``, etc.
#. Add the following line to the end of the file:

   .. code-block:: bash

      export GITHUB_TOKEN=<your-personal-access-token>
#. Save the file and run the following command to apply the changes:

   .. code-block:: bash

      source ~/.bashrc
#. Done!

Create configuration files
--------------------------

Configuration files are used to simplify inputs required to specify which repositories the issue should be broadcast to. The complete configurations are divieded into two parts and stored in ``repos.json`` and ``groups.json`` files.

.. note::

    You may also use ``repos.yaml`` or ``repos.yml`` instead of ``repos.json``. The same applies to ``groups.json``.

Example of ``repos.json``

.. code-block:: text

    {
        "<repo1>": "https://github.come/<org-name>/<repo1>",
        "<repo2>": "https://github.come/<org-name>/<repo2>",
        "<repo3>": "https://github.come/<org-name>/<repo3>",
        "<repo4>": "https://github.come/<org-name>/<repo4>",
        ...
    }

Example of ``groups.json``

.. code-block:: text

    {
        "even_group" : ["<repo2>", "<repo4>", ...],
        "odd_group" : ["<repo1>", "<repo3>", ...],
    }

``scikit-package`` will look for the configuration files in this order:

#. The GitHub repository URL or directory path provided by ``--url-to-repo-info``.
#. Current working directory.
#. The GitHub repository URL or directory path specified by the variable ``url_to_repo_info`` set in ``~/.skpkgrc``.

In the next sections, we will show you how to use the command under different scenarios.

Example usage
-------------

Suppose **Mr Neutron** wants to broadcast an issue with issuer number ``42`` in the repository ``source-repo`` to  ``repo1`` and ``repo2``. Since it is the first time **Mr Neutron** use this functionality, he choose the simplest way:

Use the configuration files in the current working directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Mr Neutron** create two files in the current working directory

    - ``repos.json``

        .. code-block:: text

            {
                "repo1": "https://github.come/MrNeutron/repo1",
                "repo2": "https://github.come/MrNeutron/repo2"
            }

    - ``groups.json``

        .. code-block:: text

            {
                "tmp_group" : ["repo1", "repo1"]
            }


#. **Mr Neutron** run the command:

   .. code-block:: bash

        package broadcast https://github.come/MrNeutron/source-repo/issues/42 tmp_group

#. The program runs in ``dry-run`` mode by default. After examining the output and finding everything is correct, **Mr Neutorn** adds the ``--dry-run n`` in the command:

   .. code-block:: bash

        package broadcast https://github.come/MrNeutron/source-repo/issues/42 tmp_group --dry-run n

#. Done! The issue is created in both ``repo1`` and ``repo2``.


It works, but creating new configuration files every time **Mr. Neutron** wants to broadcast an issue would be very inconvenient. Therefore, he decides to organize and store the repository information for future use in a GitHub repository. **Mr. Neutron** does the following:

Use the configuration files in a GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Mr Neutron** create a GitHub repository called ``repo-info``. Please see :ref:`create-new-github-repo` for more information.
#. **Mr Neutron** organizes and classifies his repositories information in ``repos.json`` and ``groups.json`` files as below, so it can be better reused:

    - ``repos.json``

        .. code-block:: text

            {
                "repo1": "https://github.come/MrNeutron/repo1",
                "repo2": "https://github.come/MrNeutron/repo2",
                "repo3": "https://github.come/MrNeutron/repo3",
                "repo4": "https://github.come/MrNeutron/repo4",
                "repo101": "https://github.come/MrNeutron/repo101",
                "repo102": "https://github.come/MrNeutron/repo102"
            }

    - ``groups.json``

        .. code-block:: text

            {
                "even_group" : ["repo2", "repo4", "repo102"],
                "odd_group" : ["repo1", "repo3", "repo101"],
                "small_group" : ["repo1", "repo2", "repo3", "repo4"],
                "large_group" : [ "repo101", "repo102"],
                "prime_group" : ["repo2", "repo3"],
                "divisible_by_3_group" : ["repo3", "repo102"],
                ...
            }

#. **Mr Neutron** updates these two files in the ``repo-info`` repository.
#. Done!

Now, suppose **Mr Neutron** needs to broadcast another issue with issue number ``43`` in the repository ``source-repo`` to  ``repo1``, ``repo2``, ``repo3``, and ``repo4``.

#. **Mr Neutron** simply run the command:

   .. code-block:: bash

        package broadcast https://github.come/MrNeutron/source-repo/issues/43 small_group --url-to-repo-info https://github.come/MrNeutron/repo-info

#. After examining the output in the ``dry-run`` mode and finding everything is correct, **Mr Neutron** adds the ``--dry-run n`` in the command:

   .. code-block:: bash

        package broadcast https://github.come/MrNeutron/source-repo/issues/43 small_group --url-to-repo-info https://github.come/MrNeutron/repo-info --dry-run n
#. Done! The issue is created in ``repo1``, ``repo2``, ``repo3``, and ``repo4``.


.. note::

    You can also provide the path to the directory containing configuration files at the top level using the ``--url-to-repo-info`` argument.


**Mr. Neutron** is still a bit unsatisfied, as he must provide the URL of the ``repo-info`` repository every time he wants to broadcast an issue. To avoid repeated typing, he decides to store the URL in ``~/.skpkgrc``:

Use the configuration files specified in ``~/.skpkgrc``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Mr Neutron** open the ``~/.skpkgrc`` file in a text editor.
#. **Mr Neutron** edit the file to include the following line:

   .. code-block:: text

    {
        # other configurations
        # ...
        "url_to_repo_info": "https://github.come/MrNeutron/repo-info"
    }

#. Save the file and done!

Suppose **Mr Neutron** needs to broadcast another issue with issue number ``44`` in the repository ``source-repo`` to  ``repo101`` and ``repo102``.

#. After making sure there are no ``repos.json`` and ``groups.json`` files in the current directory, **Mr Neutron** simply run the command:

   .. code-block:: bash

        package broadcast https://github.come/MrNeutron/source-repo/issues/44 large_group

#. The output in ``dry-run`` mode shows that everything is correct, so **Mr Neutron** adds ``--dry-run n`` in the command:

   .. code-block:: bash

        package broadcast https://github.come/MrNeutron/source-repo/issues/44 large_group --dry-run n


#. Done! The issue is created in ``repo101`` and ``repo102``.

.. note::

    If there are ``repos.json`` and ``groups.json`` files in the current working directory, ``scikit-package`` will use these files instead of the ones specified in ``~/.skpkgrc``.


.. note::

    You may also set the variable ``url_to_repo_info`` to a directory path in ``~/.skpkgrc`` if you prefer to store the configuration files locally.

**Mr Neutron** is very happy that he can now broadcast GitHub issues to multiple repositories so easily with ``scikit-package``!
