**Added:**

* <news item>

**Changed:**

* <news item>

**Deprecated:**

* <news item>

**Removed:**

* <news item>

**Fixed:**

* Add ``pip`` to the documented ``conda create`` command. Python 3.14 environments do not include it by default, so the following ``pip install`` step failed with "command not found".
* Local development installs now use ``pip install -e . --no-deps --no-build-isolation`` with the build backend installed from conda-forge, so no package is downloaded from PyPI. Previously pip fetched ``setuptools`` and ``setuptools-git-versioning`` from PyPI through build isolation despite ``--no-deps``.

**Security:**

* <news item>
