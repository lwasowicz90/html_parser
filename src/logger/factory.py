"""Creates root logger and handlers
"""
import datetime
import logging

from config import CONFIG


DEFAULT_LOG_LEVEL = logging.DEBUG
FILENAME_DT_FORMAT = "%d_%m_%Y_%H_%M_%S"
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def init():
    """Initializes logger
    """
    root_logger = logging.getLogger('root')
    log_level = getattr(logging, CONFIG.log_level, DEFAULT_LOG_LEVEL)
    root_logger.setLevel(log_level)

    if CONFIG.log_to_stdout:
        root_logger.addHandler(create_stream_handler(log_level))
        root_logger.debug('Added stdout handler to logger')
    if CONFIG.log_to_file:
        root_logger.addHandler(create_file_handler(log_level))
        root_logger.debug('Added file handler to logger')

    root_logger.info('Initialized logger, level: %s', logging.getLevelName(log_level))


def create_stream_handler(level: int) -> logging.StreamHandler:
    """Factory function for logging stream handler    
    """
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    return stream_handler


def create_file_handler(level: int) -> logging.FileHandler:
    """Factory function for logging file handler    
    """
    filename = get_filename()
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    return file_handler


def get_filename() -> str:
    """Helper method to construct log filename
    :return: filename
    """
    return f'log_{datetime.datetime.now(datetime.UTC).strftime(FILENAME_DT_FORMAT)}.txt'
