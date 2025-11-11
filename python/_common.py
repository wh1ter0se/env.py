import os
import re
import subprocess
import datetime as dt


class UvVersionInfo:
    version: str | None
    hash: str | None
    build_date: str | None

    _stdout: bytes

    def __init__(self, stdout: bytes) -> None:
        # Store stdout
        self._stdout = stdout

        # Parse the output
        output = self._stdout.decode("utf-8").strip()
        pattern = r"^uv\s+(\S+)\s+\((\S+)\s+(\d{4}-\d{2}-\d{2})\)$"
        match = re.match(pattern=pattern, string=output)
        if match is None:
            self.version = None
            self.hash = None
            self.build_date = None
            return

        # Store the fields if the regex got parsed
        self.version, self.hash, self.build_date = match.groups()

    def __str__(self) -> str:
        if self.version is None or self.hash is None or self.build_date is None:
            return "\tUnable to extract uv version information"

        return (
            f"\tVersion: {self.version}\n"
            f"\tBuild Hash: {self.hash}\n"
            f"\tBuild Date: {self.build_date}"
        )


def must_pass(value: bool) -> None:
    """Exit the program if the value is False."""
    if not value:
        print("[-] Exiting...")
        exit(1)


def format_prefix(prefix: str | None) -> str:
    """Format the prefix for logging."""
    if prefix is None:
        return "\t"
    return f"[{prefix}] "


def run_cmd(
    args: list[str],
    check: bool = False,
    stdout: int = subprocess.PIPE,
    stderr: int = subprocess.PIPE,
    shell: bool = False,
) -> subprocess.CompletedProcess:
    """Run a command and return the completed process."""
    return subprocess.run(
        args=args,
        check=check,
        stdout=stdout,
        stderr=stderr,
        shell=shell,
    )


def user_is_running_windows() -> bool:
    """Check if the user is running Windows."""
    return os.name == "nt"


def get_uv_version(prefix: str | None = None) -> UvVersionInfo | None:
    """Check if uv is installed."""
    print(format_prefix(prefix) + "Checking uv version...")
    try:
        # Check the version
        version_check_subproc = run_cmd(
            args=["uv", "--version"],
            check=True,
        )
        print("\tFound uv version")
        version = UvVersionInfo(stdout=version_check_subproc.stdout)
        print(str(version))
        return version
    except subprocess.CalledProcessError:
        print("\tNo installations of uv found")
        return None
