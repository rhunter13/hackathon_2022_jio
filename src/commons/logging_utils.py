import logging
from jio.toolkit.logging.standard_logger import StdLogFactory
from src.commons.settings import LoggingSettings


settings = LoggingSettings()
StdLogFactory.configure_standard_logger(
    logger_name=settings.LOGGER_NAME,
    service_name=settings.SERVICE_NAME,
    logging_level=settings.LOGGING_LEVEL,
)


def get_logger(logger_name=settings.LOGGER_NAME):
    return logging.getLogger(logger_name)
