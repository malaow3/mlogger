from loguru import logger
import sys


def init_logger(use_extra: bool = False):
    logger.remove()
    fmt = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {function} - {file}:{line} - {message}"
    if use_extra:
        fmt = fmt + " - {extra}"
    logger.add(
        sys.stdout,
        format=fmt,  # noqa
        level="INFO",
    )
    return logger
