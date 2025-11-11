from _common import must_pass, get_uv_version
from install_uv import install_uv, update_uv
from create_venv import create_venv
from install_dependencies import install_projects

if __name__ == "__main__":
    # Install uv
    if get_uv_version(prefix="1/4") is None:
        must_pass(install_uv(prefix="2/4"))

    # Update uv
    must_pass(update_uv(prefix="3/4"))

    # Verify installation
    must_pass(get_uv_version(prefix="4/4"))

    # Create a virtual environment
    must_pass(create_venv(prefix="5/3"))

    # Install dependencies in the virtual environment
    install_projects()

    # Generate stubs
