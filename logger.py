import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from config import LOG_DIR
import traceback

LOG_FILE = os.path.join(LOG_DIR, "error.log")

# Configura logger padrão Python com rotação diária
logger = logging.getLogger("pydefi")
logger.setLevel(logging.ERROR)
if not logger.hasHandlers():
    handler = TimedRotatingFileHandler(LOG_FILE, when="midnight", backupCount=30, encoding="utf-8")
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def log_info(msg):
    logger.info(msg)

def log_warning(msg):
    logger.warning(msg)

def log_debug(msg):
    logger.debug(msg)

def log_exception(exc: Exception, context: str = ""):
    logger.error(f"{context}\n{exc}", exc_info=True)
