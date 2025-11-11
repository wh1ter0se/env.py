import subprocess
from _config import PROJECTS
from _common import format_prefix, run_cmd
from pathlib import Path


def install_projects(
    projects: list[Path] = PROJECTS,
    prefix: str | None = None,
) -> bool:
    print(format_prefix(prefix) + "Installing dependencies...")
    for path in projects:
        try:
            print(f"\tInstalling project '{path}'...")
            run_cmd(["uv", "pip", "install", str(path)])
            print(f"\tInstalled project '{path}'")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"\tFailed to install project '{path}'")
            return False
    return True
