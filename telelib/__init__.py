__VERSION__ = open('VERSION').read().strip()

__all__ = ["TeleLib", "main_path"]


import asyncio
import datetime
import os
import logging as lg
import coloredlogs
from thread_py import ThreadPy
from telelib.tools.code_generator import CodeGenerator
from telelib.tools.scraper import Scraper

main_path = os.path.realpath(
    os.path.dirname(__file__) + '/../'
)


class TeleLib:
    _thread = None
    token = None
    api_url = "https://api.telegram.org/bot"
    _event_loop = None
    _instance = None

    debug = False
    logger = None

    def __repr__(self) -> str:
        return (f"TeleLib v{__VERSION__}")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, token=None, api_url=None, debug=True):
        if token is not None:
            TeleLib.token = token

        if api_url is not None:
            TeleLib.api_url = api_url

        TeleLib._thread = ThreadPy()
        TeleLib.debug = debug

        TeleLib._event_loop = asyncio.new_event_loop()
        TeleLib._event_loop.set_debug(debug)
        TeleLib.logger = self.Logger()

    @property
    def event_loop(self):
        return self._event_loop

    def AsyncRun(self, func, data):
        asyncio.run_coroutine_threadsafe(func(data), self.event_loop)

    class Logger:
        _instance = None
        _ = None

        class LogLevel:
            DEBUG = lg.DEBUG
            INFO = lg.INFO
            WARNING = lg.WARNING
            ERROR = lg.ERROR
            CRITICAL = lg.CRITICAL
            FATAL = lg.FATAL
            WARN = lg.WARN
            NOTSET = lg.NOTSET

        format = "%(asctime)s [%(levelname)s] " \
            "[%(processName)s -> %(threadName)s] => | %(message)s"
        formatter = lg.Formatter(format)

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            self._ = self.get_logger(name="TeleLib")

        @classmethod
        def setup_logger(cls, name, log_file, level=LogLevel.INFO):

            handler = lg.FileHandler(log_file)
            handler.setFormatter(cls.formatter)

            logger = lg.getLogger(name)
            logger.setLevel(level)
            logger.addHandler(handler)

            return logger

        @classmethod
        def get_logger(
            cls,
            level: int = LogLevel.INFO,
            name="DEFAULT_LOGGER"
        ):
            if not os.path.exists("./logs/"):
                os.makedirs("./logs/")
                print(f"Created a directory at `./logs/`")

            if name is None:
                name = "NULL_LOGGER"

            today = datetime.date.today()

            lgr = cls.setup_logger(
                name=name,
                log_file=(
                    f'./logs/{today.strftime("%Y-%m-%d")}-{name}.log'
                ),
                level=level
            )

            levels = {
                cls.LogLevel.DEBUG: "DEBUG",
                cls.LogLevel.INFO: "INFO",
                cls.LogLevel.WARNING: "WARNING",
                cls.LogLevel.ERROR: "ERROR",
                cls.LogLevel.CRITICAL: "CRITICAL",
                cls.LogLevel.FATAL: "FATAL",
                cls.LogLevel.WARN: "WARN",
                cls.LogLevel.NOTSET: "NOTSET",
            }

            coloredlogs.install(
                logger=lgr,
                fmt=cls.format,
                level=levels[level]
            )
            return lgr

        def lgr(self) -> lg.Logger:
            if self._ is None:
                self()

            return self._

        def __call__(self, *args, **kwds):
            return self._.info(msg=" ".join(args), **kwds)

    class Bot:
        @classmethod
        def start(cls):
            TeleLib.logger("Starting TeleLib Bot")

    class Telegram:
        ...

    class Types:
        ...

    # Extra Python Tools

    class Tools:
        documents_path = "https://core.telegram.org/bots/api"

        @staticmethod
        def ScraperRun():
            return Scraper().run("min.json")

        @staticmethod
        def CodeGeneratorRun():
            return CodeGenerator().run("min.json")
