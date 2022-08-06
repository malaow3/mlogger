from loguru import logger
import sys


def init_logger():
    logger.remove()
    fmt = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {function} - {file}:{line} - {message}"
    if len(logger.__dict__["_options"][-1]) != 0:
        fmt = fmt + " - {extra}"
    logger.add(
        sys.stdout,
        format=fmt,  # noqa
        level="INFO",
    )
    return logger
