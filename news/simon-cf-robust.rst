**Added:**

* <news item>

**Changed:**

* Rewrote the ``package update conda-forge`` documentation to explain what the command automates and what it deliberately leaves to the user, the one-time fork/clone/remote setup it expects, the git operations it performs, its rollback behaviour, and a troubleshooting table of its error messages.
* Use ``pathlib.Path`` instead of ``os.path`` for path handling in the conda-forge update command.
* Renamed the internal ``cf`` module to ``conda_forge`` for readability. No change to the ``package update conda-forge`` CLI.

**Deprecated:**

* <news item>

**Removed:**

* <news item>

**Fixed:**

* Skip feedstocks that cannot be resolved on PyPI instead of aborting the whole listing, and list feedstocks in a stable sorted order.
* Check that the GitHub CLI is installed before any changes are made, instead of failing after the branch has already been pushed.
* Restore the feedstock clone to its original branch when any step of ``package update conda-forge`` fails, rather than leaving a half-finished branch behind.
* Only rewrite the ``sha256`` of the top-level ``source`` section of ``meta.yaml``. Recipes with several sources, or with the hash held in a Jinja variable, are no longer corrupted.
* Verify that the ``upstream`` remote points at the expected feedstock rather than only checking that a remote of that name exists.
* Look up the default branch of the upstream feedstock instead of assuming ``main``, so feedstocks on ``master`` or any other default branch work.
* No longer discard uncommitted work in the feedstock clone. ``package update conda-forge`` used to run ``git stash`` without ever restoring it; it now refuses to run on a dirty clone and tells you to commit or stash first.

**Security:**

* <news item>
