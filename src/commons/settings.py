"""
Settings from env variables
"""
import os
from pydantic import BaseSettings
from typing import Optional, List


class LoggingSettings(BaseSettings):
    """
    Logging Settings from env variables
    """

    SERVICE_NAME: str = "developer-portal"
    LOGGER_NAME: str = "developer_portal_logger"
    LOGGING_LEVEL: str = "INFO"

MYSQL_CONNECTION_STRING = os.environ.get("MYSQL_CONNECTION_STRING", None)