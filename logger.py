import logging
import os
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Final


@dataclass
class LoggedStatuses:
    warning: bool = False
    failed: bool = False
    blocked: bool = False


class Logger:
    LOG_FORMAT: Final[str] = '%(asctime)s %(levelname)s:\t%(message)s'
    DATE_FORMAT: Final[str] = "%Y/%m/%d %H:%M:%S"
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")

    LOG_NAME: Final[str] = f"log{current_time}.txt"
    LOG_PATH: Final[str] = fr"C:\tmp\DayzBot"
    __instance = None
    statuses_called = LoggedStatuses()

    @classmethod
    def warning(cls, msg: str) -> None:
        cls.statuses_called.warning = True
        cls.__get_logger().warning(msg)

    @classmethod
    def info(cls, msg: str) -> None:
        cls.__get_logger().info(msg)

    @classmethod
    def __get_log_files(cls, suffix: str = "") -> str:
        log_filename = f"{cls.LOG_NAME}{suffix}.txt"
        log_file_path = os.path.join(cls.LOG_PATH, log_filename)
        return log_file_path

    @staticmethod
    def __get_handler(output: Any, log_level: int, formatter: logging.Formatter) -> logging.FileHandler:
        handler = logging.FileHandler(output) if type(output) == str else logging.StreamHandler(output)
        handler.setLevel(log_level)
        handler.setFormatter(formatter)
        return handler

    @classmethod
    def __prepare_log_files(cls) -> None:
        log_file_path = cls.__get_log_files()
        cls.__create_file(log_file_path)

    @classmethod
    def __get_logger(cls) -> logging.Logger:
        if cls.__instance is None:
            cls.__create_logger()
        return cls.__instance

    @classmethod
    def __create_logger(cls) -> None:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.handlers = []
        cls.__prepare_log_files()
        log_file_path = cls.__get_log_files()
        formatter = logging.Formatter(Logger.LOG_FORMAT, Logger.DATE_FORMAT)
        for output, log_level in [(log_file_path, logging.INFO),
                                  (sys.stdout, logging.INFO)]:
            logger.addHandler(Logger.__get_handler(output, log_level, formatter))
        cls.__instance = logger

    @staticmethod
    def __create_file(file_path: str, file_name: str = None) -> None:
        if file_name:
            file_path = os.path.join(file_path, file_name)
        open(file_path, 'a').close()
