import shutil
from pathlib import Path


def _detect_import_and_module_path():
    import_name = Path.cwd().name.replace("-", "_")
    module_path = Path("src") / Path(
        import_name.replace(".", "/").replace("-", "_")
    )
    return import_name, module_path.resolve()


def _generate_api_doc(
    package_name, package_dir, api_dir=Path("docs/source/api")
):
    eq_spacing = "=" * len(f"{package_name} package")
    subpkg = f""":tocdepth: -1

{package_name.replace('_', '-')} package
{eq_spacing}

.. automodule:: {package_name}
    :members:
    :undoc-members:
    :show-inheritance:
"""
    # Tag all subpackages
    subpkg_names = []
    subpkg_paths = []
    skip_dirs = [
        "tests",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        ".git",
    ]
    for child in package_dir.iterdir():
        if child.is_dir() and child.name not in skip_dirs:
            subpkg_names.append(f"{package_name}.{child.name}")
            subpkg_paths.append(child)
    if len(subpkg_names) > 0:
        subpkg += """
Subpackages
-----------

.. toctree::
    :titlesonly:

"""
        for subpkg_name in subpkg_names:
            subpkg += f"    {subpkg_name}\n"
    # Tag all submodules
    submodule_names = []
    skip_files = ["__init__", "version"]
    for child in package_dir.iterdir():
        if (
            child.is_file()
            and child.suffix == ".py"
            and child.stem not in skip_files
        ):
            submodule_names.append(f"{package_name}.{child.stem}")
    if len(submodule_names) > 0:
        subpkg += """
Submodules
----------
"""
    for submodule_name in submodule_names:
        dsh_spacing = "^" * len(f"{submodule_name} module")
        subpkg += f"""
{submodule_name} module
{dsh_spacing}

.. automodule:: {submodule_name}
    :members:
    :undoc-members:
    :show-inheritance:
"""

    subpkg = subpkg.rstrip() + "\n"  # clean ending
    package_file = api_dir / f"{package_name}.rst"
    with open(package_file, "w") as pfile:
        pfile.write(subpkg)
    # Recurse on all subpackages
    for idx, path in enumerate(subpkg_paths):
        _generate_api_doc(subpkg_names[idx], path)


def _clean_api_dir(api_dir=Path("docs/source/api")):
    """Delete and recreate the API directory."""
    if api_dir.exists():
        shutil.rmtree(api_dir)
    api_dir.mkdir(parents=True)


def build(args):
    """Entry point for the auto API documentation generation script.

    This script detects the package import name and module path, cleans
    the API directory, and generates the API documentation for the
    package and its subpackages.
    """
    _clean_api_dir()
    import_name, module_path = _detect_import_and_module_path()
    if not module_path.is_dir():
        raise SystemExit(f"Package directory not found: {module_path}")
    _generate_api_doc(import_name, module_path)
