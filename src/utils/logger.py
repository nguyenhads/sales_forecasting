import logging
from logging import INFO, FileHandler, Formatter, StreamHandler, getLogger
from pathlib import Path
from typing import Union


def init_logger(log_file: Union[str, Path]) -> logging.Logger:
    """Initialize logger.

    Parameters:
    - log_file (Union[str, Path]): Path to the log file.

    Returns:
    - logging.Logger: Logger instance.
    """
    # Create logger
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create handlers
    stream_handler = StreamHandler()
    file_handler = FileHandler(filename=str(log_file))

    # Set logger format
    formatter = Formatter("[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)")
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger
