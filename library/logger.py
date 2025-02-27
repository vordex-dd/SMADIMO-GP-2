import logging
import logging.config


class LoggerSettings:
    @staticmethod
    def set_up():
        logging.config.fileConfig('./../logging.conf')
