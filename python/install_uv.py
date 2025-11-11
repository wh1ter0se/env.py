import subprocess
from _common import format_prefix, run_cmd, user_is_running_windows, get_uv_version


def install_uv(prefix: str | None) -> bool:
    """Install uv, if not already installed."""
    print(format_prefix(prefix) + "Installing uv...")

    # Install via curl if we can
    if not user_is_running_windows():
        print("\t*nix detected, installing uv via curl...")
        try:
            run_cmd(
                args=["curl", "-LsSf", "https://astral.sh/uv/install.sh", "|", "sh"],
                check=True,
            )
            run_cmd(
                args=["uv", "--version"],
                check=True,
            )
            print("\tSuccessfully installed uv via curl")
            return True
        except subprocess.CalledProcessError:
            print("\tFailed to install uv via curl")

    # Install via pip on Windows or if curl fails
    print("\tInstalling uv via pip...")
    try:
        run_cmd(
            args=["pip", "install", "uv"],
            check=True,
        )
        run_cmd(
            args=["uv", "--version"],
            check=True,
        )
        print("\tSuccessfully installed uv via pip")
        return True
    except subprocess.CalledProcessError:
        print("\tFailed to install uv via pip.")

    return False


def update_uv(prefix: str | None) -> bool:
    """Update uv to the latest version."""
    print(format_prefix(prefix) + "Updating uv...")

    # Early exit if uv is not installed
    if get_uv_version() is None:
        return False

    # Update through uv
    print("\tUpdating uv directly...")
    try:
        run_cmd(
            args=["uv", "self-update"],
            check=True,
        )
        print("\tSuccessfully updated uv directly")
        return True
    except subprocess.CalledProcessError:
        print("\tFailed to update uv directly")

    # Update through pip
    print("\tUpdating uv via pip...")
    try:
        run_cmd(
            args=["pip", "install", "--upgrade", "uv"],
            check=True,
        )
        print("\tSuccessfully updated uv via pip")
        return True
    except subprocess.CalledProcessError:
        print("\tFailed to update uv via pip")

    return False


if __name__ == "__main__":
    # Install uv
    uv_installed = get_uv_version(prefix="1/4")
    if not uv_installed:
        install_uv(prefix="2/4")

    # Update uv
    update_uv(prefix="3/4")

    # Verify installation
    get_uv_version(prefix="4/4")
