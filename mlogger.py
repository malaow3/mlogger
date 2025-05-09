import logging
import sys
from typing import cast

from loguru import logger
from pylogrus import PyLogrus, TextFormatter


def get_logger() -> PyLogrus:
    logging.setLoggerClass(PyLogrus)

    logger: PyLogrus = cast(PyLogrus, logging.getLogger(__name__))
    logger.setLevel(logging.DEBUG)

    # get file line and function
    format = (
        "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(funcName)s - %(message)s"
    )
    formatter = TextFormatter(fmt=format, datefmt="Z", colorize=True)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


log: PyLogrus = get_logger()


def init_logger(use_extra: bool = False):
    logger.remove()
    fmt = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {function} - {file}:{line} - {message}"
    if use_extra:
        fmt = fmt + " - {extra}"
    _ = logger.add(
        sys.stdout,
        format=fmt,  # noqa
        level="INFO",
    )
    return logger
