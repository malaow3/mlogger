from loguru import logger
import sys


def init_logger():
    logger.remove()
    logger.add(
        sys.stdout,
        format='<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {function} - {file}:{line} - {message}',  # noqa
        level='INFO')
    return logger
