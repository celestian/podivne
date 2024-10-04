import os
from pathlib import Path

import nox

# It's a good idea to keep your dev session out of the default list
# so it's not run twice accidentally
nox.options.sessions = [
    "behave-3.12",
]  # Sessions other than 'dev'


# this VENV_DIR constant specifies the name of the dir that the `dev`
# session will create, containing the virtualenv;
# the `resolve()` makes it portable
VENV_DIR = Path("./.venv").resolve()

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=["3.12"])
def dev(session: nox.Session) -> None:
    """
    Sets up a python development environment for the project.

    This session will:
    - Create a python virtualenv for the session
    - Install the `virtualenv` cli tool into this environment
    - Use `virtualenv` to create a global project virtual environment
    - Invoke the python interpreter from the global project environment to install
      the project and all it's development dependencies.
    """

    session.install("virtualenv")
    # the VENV_DIR constant is explained above
    session.run("virtualenv", os.fsdecode(VENV_DIR), silent=True)

    python = os.fsdecode(VENV_DIR.joinpath("bin/python"))

    # Use the venv's interpreter to install the project along with
    # all it's dev dependencies, this ensures it's installed in the right way
    session.run(python, "-m", "pip", "install", "-e", ".[dev]", external=True)

    print("\n--------------------------------------------")
    print('Activate your "development" environemt with:')
    if os.name == "posix":
        print("    source .venv/bin/activate")
    else:
        print(r"    .venv\Scripts\activate")
    print("--------------------------------------------\n")


@nox.session(python=["3.12"])
def behave(session: nox.Session) -> None:
    """Run behave tests"""
    
    session.install("virtualenv")
    session.run("virtualenv", os.fsdecode(VENV_DIR), silent=True)
    python = os.fsdecode(VENV_DIR.joinpath("bin/python"))
    session.run(python, "-m", "pip", "install", ".", external=True)

    session.install("behave")

    debug = "1"
    if debug and "1" == debug:
        session.run(
            "behave",
            "-v",
            "--no-capture",
            "--no-capture-stderr",
            "features/",
        )
    else:
        session.run("behave", "features/")
