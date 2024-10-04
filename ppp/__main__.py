"""PPP

Usage:
  ppp run
  ppp (-h | --help)
  ppp --version

Options:
  --cfg=<cfg_file>  Configuration file [default: ./rpgt.conf].
  -h --help         Show this screen.
  --version         Show version.
"""

import logging
import os
import sys
from pathlib import Path
from docopt import docopt

from ppp._version import __version__
from ppp.core.app import App
from ppp.core.logger import Logger


def main():

    _logger = Logger().logger
    _logger.info("Main started")

    args = docopt(__doc__, version=__version__)

    cwd = Path(os.getcwd()).resolve()
    log_file = cwd.joinpath("ppp.log")
    print(f">>> Log_file based on cwd [{log_file}] <<<")


    if args['run']:
        app = App()
        app.do()    

    sys.exit(0)


if __name__ == "__main__":
    _logger = Logger().logger

    try:
        main()
    except Exception as e:  # pylint: disable=broad-except
        _logger.exception("Unexpected exception: [%s]", e)
