import logging
import logging.config


class Logger:
    @staticmethod
    def set_up_logger():
        logging.config.fileConfig('logging.conf')