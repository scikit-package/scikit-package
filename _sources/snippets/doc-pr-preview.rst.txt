#. Visit https://app.readthedocs.org/.

#. Click :guilabel:`Log in using GitHub`.

#. If your repository is under a GitHub organization, follow the extra steps below:

    #. Visit https://github.com/settings/applications

    #. Click the :guilabel:`Read the Docs Community` application.

    #. Click the :guilabel:`Request` button for the organization under :guilabel:`Organization Access`,

    #. Done. Now, Read the Docs can import repositories in the GitHub organization.

#. Visit https://app.readthedocs.org/dashboard/import/.

#. Enter the :guilabel:`Repository name`.

#. Click :guilabel:`Continue`.

#. Visit your project page, e.g., https://app.readthedocs.org/projects/bobleesjrelease/.

#. Click :guilabel:`Settings`.

#. Click :guilabel:`Pull request builds` under :guilabel:`Building` on the left menu.

#. Enable :guilabel:`Build pull requests for this project`.

#. Click :guilabel:`Update`.

    .. image:: ../img/doc-pr-preview-setup.png
      :alt: doc-pr-preview-setup
      :width: 600px

#. Done! Now, in each PR, you will see the following workflow triggered. You can click on the workflow to view its rendered documentation online.

    .. image:: ../img/doc-pr-preview-setup-ci.png
      :alt: doc-pr-preview-setup-ci
      :width: 600px

.. tip::

  Press the :guilabel:`d` key on your keyboard to view the changes! e.g., https://bobleesjrelease--1.org.readthedocs.build/en/1/
