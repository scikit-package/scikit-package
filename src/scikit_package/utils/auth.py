import subprocess


def get_github_username():
    """Get the GitHub username using the GitHub CLI."""
    try:
        username = subprocess.check_output(
            ["gh", "api", "user", "--jq", ".login"], text=True
        ).strip()
        return username
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise RuntimeError(
            "Could not retrieve GitHub username using GitHub CLI. "
            "Please make sure the GitHub CLI ('gh') is installed and that "
            "your local machine is authenticated by running 'gh auth login'."
        )


def get_current_branch(cwd=None):
    result = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True, cwd=cwd
    )
    return result.strip()
