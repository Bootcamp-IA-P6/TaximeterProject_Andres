import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    handler = RotatingFileHandler(
        "logs/taximeter.log",
         maxBytes = 200000,
         backupCount=5
    )

    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        handlers=[handler]
    )

    logging.info("Logging system initialized")