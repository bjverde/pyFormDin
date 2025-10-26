import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import traceback

class LogHelper:
    def __init__(self, log_dir, logger_prefix=None):
        log_file = os.path.join(log_dir, "error.log")
        prefix = logger_prefix if logger_prefix is not None else "pyFormDin_"
        self.logger = logging.getLogger(f"{prefix}{id(self)}")
        self.logger.setLevel(logging.ERROR)
        if not self.logger.hasHandlers():
            handler = TimedRotatingFileHandler(log_file, when="midnight", backupCount=30, encoding="utf-8")
            formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log_info(self, msg):
        self.logger.info(msg)

    def log_warning(self, msg):
        self.logger.warning(msg)

    def log_debug(self, msg):
        self.logger.debug(msg)

    def log_exception(self, exc: Exception, context: str = ""):
        self.logger.error(f"{context}\n{exc}", exc_info=True)
