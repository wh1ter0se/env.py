from _common import must_pass
from install_uv import install_uv, update_uv
from create_venv import create_venv

if __name__ == "__main__":
    # Install uv
    must_pass(install_uv(prefix="1/3"))
    must_pass(update_uv(prefix="2/3"))

    # Create a virtual environment
    must_pass(create_venv(prefix="3/3"))

    # Install dependencies in the virtual environment

    # Generate stubs

    # Generate package
