import sys

from loguru import logger

LOG_LVL = "INFO"
APP_LOGGER_NAME = "azure_helper"
LOG_FILE = "./mlops_e2e_pipeline.log"


def get_logger():
    """_summary_

    Returns:
        _type_: _description_
    """

    fmt = (
        "<level>{level: <8}</level> - "
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> - "
        f"{APP_LOGGER_NAME} - "
        "<cyan>{process}</cyan> - "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )
    config = {
        "handlers": [
            {"sink": sys.stdout, "format": fmt, "level": LOG_LVL},
            {"sink": LOG_FILE, "serialize": True, "format": fmt},
        ],
    }
    logger.configure(**config)

    return logger
