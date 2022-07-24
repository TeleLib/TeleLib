__VERSION__ = open('VERSION').read().strip()

__all__ = ["TeleLib", "main_path"]


import asyncio
import os
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

    @property
    def event_loop(self):
        return self._event_loop

    class Logger:
        ...

    class Bot:
        ...

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
