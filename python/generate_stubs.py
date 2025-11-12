from _config import PROJECTS
from _common import must_pass
from pathlib import Path


def generate_stubs(
    projects: list[Path] = PROJECTS,
    prefix: str | None = None,
) -> bool:
    for project in projects:
        # Generate stubs for each project
        pass
    return True


if __name__ == "__main__":
    # Generate stubs
    must_pass(generate_stubs(prefix="7/7"))
