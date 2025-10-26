import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import traceback

class LogHelper:
    def __init__(self, log_dir, logger_prefix=None):
        prefix = logger_prefix if logger_prefix is not None else "pyFormDin_"
        self.logger = logging.getLogger(f"{prefix}{id(self)}")
        self.logger.setLevel(logging.DEBUG)

        # Handler para erros
        error_file = os.path.join(log_dir, "error.log")
        error_handler = TimedRotatingFileHandler(error_file, when="midnight", backupCount=30, encoding="utf-8")
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s %(message)s'))
        self.logger.addHandler(error_handler)

        # Handler para warnings
        warning_file = os.path.join(log_dir, "warning.log")
        warning_handler = TimedRotatingFileHandler(warning_file, when="midnight", backupCount=30, encoding="utf-8")
        warning_handler.setLevel(logging.WARNING)
        warning_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s %(message)s'))
        self.logger.addHandler(warning_handler)

        # Handler para info/debug
        info_file = os.path.join(log_dir, "info.log")
        info_handler = TimedRotatingFileHandler(info_file, when="midnight", backupCount=30, encoding="utf-8")
        info_handler.setLevel(logging.INFO)
        info_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s %(message)s'))
        self.logger.addHandler(info_handler)

    def log_info(self, msg):
        self.logger.info(msg)

    def log_warning(self, msg):
        self.logger.warning(msg)

    def log_debug(self, msg):
        self.logger.debug(msg)

    def log_exception(self, exc: Exception, context: str = ""):
        self.logger.error(f"{context}\n{exc}", exc_info=True)
