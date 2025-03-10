import os
from loguru import logger
from src.settings.base import PROJECT_DIR


server_log_path = os.path.join(PROJECT_DIR, "server.log")
logger.add(server_log_path, retention="10 days", level="INFO", format="{time} {level} {message}")
