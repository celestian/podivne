from ppp.core.logger import Logger

_logger = Logger().logger


class App:

    def __init__(self):
        print('App init')
        _logger.info('App init')

    def do(self):
        print('App do')
        _logger.info('App do')
