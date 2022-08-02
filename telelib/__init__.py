import os
if os.path.exists('VERSION'):
    __VERSION__ = open('VERSION').read().strip()
else:
    __VERSION__ = "6.0.010"

__all__ = (
    '__VERSION__',
    "TeleLib",
    "Logger",
    "telegram",
    "Telegram",
)

import asyncio
import datetime
import json
import logging as lg

try:
    import httpx
except ImportError:
    try:
        import pip
        pip.main(['install', 'httpx'])
        import httpx
    except ImportError:
        print("Didn't find httpx, please install it")
        exit(1)

try:
    import coloredlogs
except ImportError:
    try:
        import pip
        pip.main(['install', 'coloredlogs'])
        import coloredlogs
    except ImportError:
        print("Didn't find coloredlogs, please install it")
        exit(1)


from typing import Any, Callable, Coroutine, \
    List, Mapping, Optional, Tuple, Union

try:
    from thread_py import ThreadPy
except ImportError:
    try:
        import pip
        pip.main(['install', 'thread_py'])
        from thread_py import ThreadPy
    except ImportError:
        print("Didn't find thread_py, please install it")
        exit(1)

from telelib.tools.code_generator import CodeGenerator
from telelib.tools.scraper import Scraper
from telelib.telegram import getUpdates
import telelib.telegram as _telegram

main_path = os.path.realpath(
    os.path.dirname(__file__) + '/../'
)


telegram = _telegram


class _Tools:
    documents_path = "https://core.telegram.org/bots/api"

    @staticmethod
    def ScraperRun():
        return Scraper().run("min.json")

    @staticmethod
    def CodeGeneratorRun():
        return CodeGenerator().run("min.json")


class Logger:
    _instance: "Logger" = None  # type: ignore
    _: lg.Logger = None  # type: ignore

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


class Telegram:
    class RequestData:
        def __init__(self, params, files={}):
            self.multipart_data = files
            self.json_parameters = params
            for key, value in self.json_parameters.copy().items():
                if value is None:
                    del self.json_parameters[key]
            for key, value in self.multipart_data.copy().items():
                if value is None:
                    del self.multipart_data[key]

        def __repr__(self) -> str:
            return f"{self.multipart_data}, {self.json_parameters}"

    USER_AGENT: str = "TelegramBotAPI/1.0"
    update_types: List[str] = [
        'message',
        'edited_message',
        'channel_post',
        'edited_channel_post',
        'inline_query',
        'chosen_inline_result',
        'callback_query',
        'shipping_query',
        'pre_checkout_query',
        'poll',
        'poll_answer',
        'my_chat_member',
        'chat_member',
        'chat_join_request',
    ]

    _instance: "Telegram" = None  # type: ignore
    token: str = None  # type: ignore
    api_url: str = None  # type: ignore
    client_args: Mapping[str, Any] = {}
    client: httpx.AsyncClient = None  # type: ignore

    def __repr__(self) -> str:
        return f"TelegramAPI(id={id(self)})"

    def __init__(self, token=None, api_url=None, proxy_url=None):
        Telegram.init(token, api_url, proxy_url)

    @classmethod
    def init(cls, token=None, api_url=None, proxy_url=None):
        if token is not None:
            Telegram.token = token
        if api_url is not None:
            Telegram.api_url = api_url
        timeout = httpx.Timeout(
            connect=10,
            read=10,
            write=10,
            pool=100,
        )
        limits = httpx.Limits(
            max_connections=100,
            max_keepalive_connections=100,
        )
        Telegram.client_args = {
            "timeout": timeout,
            "proxies": proxy_url,
            "limits": limits,
        }
        Telegram.client = httpx.AsyncClient(**cls.client_args)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    async def construct(cls):
        cls.client = httpx.AsyncClient(**cls.client_args)
        return cls.client

    @classmethod
    async def destruct(cls):
        if cls.client.is_closed:
            raise Exception("Connection is already closed.")

        await cls.client.aclose()

    async def __aenter__(self):
        await self.construct()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.destruct()

    @classmethod
    async def __req(
        cls,
        url: str,
        method: str,
        request_data: Optional[RequestData] = None,
    ) -> Tuple[int, dict]:
        if cls.client is None:
            cls.client = await cls.construct()

        if cls.client.is_closed:
            raise RuntimeError("Client is Closed.")

        files = request_data.multipart_data if request_data else None
        data = request_data.json_parameters if request_data else None

        try:
            res = await cls.client.request(
                method=method,
                url=url,
                headers={"User-Agent": cls.USER_AGENT},
                timeout=cls.client_args['timeout'],
                files=files,
                json=data
            )
        except httpx.TimeoutException as err:
            if isinstance(err, httpx.PoolTimeout):
                raise Exception("Pool is full")
            raise err
        except httpx.HTTPError as err:
            raise Exception(f"httpx HTTPError: {err}")

        return res.status_code, json.loads(res.content)

    @classmethod
    async def is_ok(cls, res: Tuple[int, dict]) -> Union[bool, dict]:
        if res[0] == 200:
            if res[1]["ok"]:
                return res[1]['result']
        return False

    @classmethod
    async def __method(
        cls,
        method: str,
        request_data: Optional[Union[RequestData, dict]] = None,
        **kwargs
    ) -> Tuple[int, dict]:

        url = f"{cls.api_url}{cls.token}/{method}"
        _method = "GET" if request_data is None else "POST"
        if request_data is None:
            request_data = cls.RequestData(kwargs)

        if isinstance(request_data, cls.RequestData):
            res = await cls.__req(
                url,
                _method,
                request_data
            )
        else:
            res = await cls.__req(
                url,
                _method,
                cls.RequestData(request_data)
            )
        return res

    @classmethod
    async def call_method(
        cls,
        method: str,
        **kwargs
    ) -> Union[bool, dict]:
        return await cls.is_ok(
            await cls.__method(
                method,
                **kwargs
            )
        )

    @classmethod
    async def __call__(
        cls,
        method: "telegram.Types.DefaultMethod"
    ) -> telegram.Types.DefaultMethod:
        _method, args = method._call()
        method._called = True
        method._res = await cls.call_method(_method, **args)
        return method


class _Bot:
    event_handlers = {}

    @classmethod
    def set_event_handler(cls, event, func):
        cls.event_handlers[event] = func

    @classmethod
    async def start(cls, offset=0):
        TeleLib.logger("Starting TeleLib Bot Instance")

        while TeleLib.is_running:
            await asyncio.sleep(0.01)
            await TeleLib.tg(updates := getUpdates(
                offset=telegram.Integer(offset))
            )

            def _(update):
                for event, event_func in cls.event_handlers.items():
                    for update_type in Telegram.update_types:
                        if type(getattr(update, update_type)) == event:
                            try:
                                ThreadPy.create_and_start_thread(
                                    name=f"{update.update_id}-T",
                                    target=TeleLib.AsyncRun,
                                    args=(
                                        event_func,
                                        getattr(update, update_type)
                                    )
                                )
                            except Exception as err:
                                print(err)

                            return True

            for update in updates.result():
                offset = update.update_id + 1
                _(update)

                if 'main' in cls.event_handlers:
                    ThreadPy.create_and_start_thread(
                        name=f"{update.update_id}-T",
                        target=TeleLib.AsyncRun,
                        args=(
                            cls.event_handlers['main'],
                            update
                        )
                    )


class TeleLib:
    Bot = _Bot()
    Tools = _Tools()
    logger = Logger()
    _thread = ThreadPy()
    tg: Telegram = None  # type: ignore

    token: str = None  # type: ignore
    api_url = "https://api.telegram.org/bot"
    _event_loop: asyncio.AbstractEventLoop = None  # type: ignore
    _instance: "TeleLib" = None  # type: ignore

    debug = True
    is_running = True

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

        TeleLib.debug = debug

        TeleLib._event_loop = asyncio.new_event_loop()
        TeleLib._event_loop.set_debug(TeleLib.debug)
        TeleLib.tg = Telegram(TeleLib.token, TeleLib.api_url)

    @property
    def event_loop(self):
        if self._event_loop is None:
            TeleLib._event_loop = asyncio.new_event_loop()
        return self._event_loop

    @classmethod
    def AsyncRun(
        cls,
        func: Callable[[Any], Coroutine[Any, Any, Any]],
        *args,
        **kwargs
    ) -> Any:
        async def runner():
            await func(*args, **kwargs)

        return asyncio.run_coroutine_threadsafe(
            runner(),
            cls._event_loop
        )

    def start(self):
        TeleLib.logger("Starting TeleLib")
        self.event_loop.run_until_complete(TeleLib.Bot.start())
