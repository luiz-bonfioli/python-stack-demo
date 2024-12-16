import logging

from src.core.common.config import APP_DEFAULT_LOG_LEVEL


def get_logger(logger_name, log_level=APP_DEFAULT_LOG_LEVEL):
    # Create a logger
    logger = logging.getLogger(logger_name)

    # Set the log level (default to DEBUG if not provided)
    logger.setLevel(logging.getLevelName(log_level))

    # Create a console handler
    console_handler = logging.StreamHandler()

    # Set a log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger
