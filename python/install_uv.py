import subprocess
from _common import (
    must_pass,
    format_prefix,
    run_cmd,
    user_is_running_windows,
    get_uv_version,
)


def install_uv(prefix: str | None) -> bool:
    """Install uv, if not already installed."""
    print(format_prefix(prefix) + "Installing uv...")

    # Install via curl if we can
    if not user_is_running_windows():
        print("\t*nix detected, installing uv via curl...")
        try:
            run_cmd(
                cmd="curl -LsSf https://astral.sh/uv/install.sh | sh",
                shell=True,
                check=False,
            )
            run_cmd(
                cmd=["uv", "--version"],
                check=True,
            )
            print("\tSuccessfully installed uv via curl")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("\tFailed to install uv via curl")

    # Install via Python's pip
    print("\tInstalling uv via pip...")
    try:
        run_cmd(
            cmd=["python", "-m", "pip", "install", "uv"],
            check=True,
        )
        run_cmd(
            cmd=["uv", "--version"],
            check=True,
        )
        print("\tSuccessfully installed uv via pip")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\tFailed to install uv via pip.")

    # Install via Python3's pip
    print("\tInstalling uv via pip3...")
    try:
        run_cmd(
            cmd=["python3", "-m", "pip", "install", "uv"],
            check=True,
        )
        run_cmd(
            cmd=["uv", "--version"],
            check=True,
        )
        print("\tSuccessfully installed uv via pip3")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\tFailed to install uv via pip3.")

    return False


def update_uv(prefix: str | None) -> bool:
    """Update uv to the latest version."""
    print(format_prefix(prefix) + "Updating uv...")

    # Update through uv
    print("\tUpdating uv directly...")
    try:
        run_cmd(
            cmd=["uv", "self", "update"],
            check=True,
        )
        print("\tSuccessfully updated uv directly")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\tFailed to update uv directly")

    # Update through Python's pip
    print("\tUpdating uv via pip...")
    try:
        run_cmd(
            cmd=["python", "-m", "pip", "install", "--upgrade", "uv"],
            check=True,
        )
        print("\tSuccessfully updated uv via pip")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\tFailed to update uv via pip")

    # Update through Python3's pip
    print("\tUpdating uv via pip3...")
    try:
        run_cmd(
            cmd=["python3", "-m", "pip", "install", "--upgrade", "uv"],
            check=True,
        )
        print("\tSuccessfully updated uv via pip3")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\tFailed to update uv via pip3")

    return False


if __name__ == "__main__":
    # Install uv
    if get_uv_version(prefix="1/4") is None:
        must_pass(install_uv(prefix="2/4"))

    # Update uv
    must_pass(update_uv(prefix="3/4"))

    # Verify installation
    must_pass(get_uv_version(prefix="4/4") is not None)
