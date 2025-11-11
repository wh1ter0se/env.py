import shutil
import subprocess
from _common import format_prefix, run_cmd
from _config import VENV_LOCATION, PYTHON_VERSION
from pathlib import Path


def create_venv(
    venv_path: Path = VENV_LOCATION,
    version: str | None = PYTHON_VERSION,
    prefix: str | None = None,
) -> str | None:
    """Create a virtual environment at the specified path."""
    print(format_prefix(prefix) + "Creating venv...")

    # Remove the existing venv
    shutil.rmtree(venv_path)

    # Specify version if provided
    cmd = ["uv", "venv"]
    if version is not None:
        cmd.append("--python")
        cmd.append(version)
    cmd.append(str(venv_path))

    # Create the venv
    try:
        run_cmd(cmd=cmd, check=True)
        print("\tVenv created")
        return venv_path
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\tFailed to create venv")
