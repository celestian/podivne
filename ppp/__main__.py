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
import atexit
from pathlib import Path

from docopt import docopt

from ppp._version import __version__
from ppp.core.app import App


def _init_logger():
    logger = logging.getLogger('app')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s: %(message)s {%(module)s:%(lineno)d}")

    cwd = Path(os.getcwd()).resolve()
    log_file = cwd.joinpath("ppp.log")

    print(f">>> AAA <<<")
    print(f">>> Logging to [{log_file}] <<<")
    file_handler = logging.FileHandler(
        filename=log_file, mode="w", encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(logging.ERROR)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    atexit.register(_shutdown_logger)


def _shutdown_logger():
        
        logger = logging.getLogger('app')
        for handler in logger.handlers:
             print(f"Flushing handler [{handler}]")
             handler.flush()
             handler.close()

        logging.shutdown()


def main():

    _logger = logging.getLogger('app')
    _logger.info("Main started")

    args = docopt(__doc__, version=__version__)

    cwd = Path(os.getcwd()).resolve()
    log_file = cwd.joinpath("ppp.log")

    print(f">>> BBB <<<")
    print(f">>> Logging to [{log_file}] <<<")


    if args['run']:
        app = App()
        app.do()    

    sys.exit(0)


if __name__ == "__main__":
    _init_logger()
    _logger = logging.getLogger('app')

    try:
        main()
    except Exception as e:  # pylint: disable=broad-except
        _logger.exception("Unexpected exception: [%s]", e)
