import logging
import sys
import os
import atexit
from pathlib import Path

from ppp.core.design_patterns import Singleton


class Logger(metaclass=Singleton):

    def __init__(self):
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(levelname)s: %(message)s {%(module)s:%(lineno)d}")

        cwd = Path(os.getcwd()).resolve()
        log_file = cwd.joinpath("ppp.log")
        #log_file = Path("/home/celestian/Projects/podivne/ppp2.log").resolve()
        
        file_handler = logging.FileHandler(
            filename=log_file, mode="w", encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_handler.setLevel(logging.ERROR)
        stream_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(stream_handler)

        atexit.register(self._shutdown_logger)

        print(f">>> Used log_file [{log_file}] <<<")

    def _shutdown_logger(self):
        
        for handler in self._logger.handlers:
             print(f"Flushing handler [{handler}]")
             handler.flush()
             handler.close()

        logging.shutdown()

    @property
    def logger(self):
        return self._logger