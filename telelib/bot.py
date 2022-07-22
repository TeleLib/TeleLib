import json
import asyncio
import httpx

from typing import Any, Callable, List, Optional, Tuple, Union
from thread_py import ThreadPy


class DefaultType:
    def __init__(self, d):
        self._d = d

    def __repr__(self) -> str:
        string = f"{self.__class__.__name__}("
        for k, v in self._d.items():
            string += f"{k}={repr(v)}, "
        return string+")"

    def __iter__(self):
        return iter(self._d)

    def __getattr__(self, __name: str) -> Any:
        return self._d[__name]

    def __getitem__(self, name):
        return self._d[name]


class RequestData:
    def __init__(self, params, files={}):
        self.multipart_data = files
        self.json_parameters = params


class TelegramAPI:
    USER_AGENT = "TelegramBotAPI/1.0"
    update_types = [
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

    instance = None
    token = None
    api_url = None
    client_args = None
    client = None
    me = None

    def __repr__(self) -> str:
        return f"TelegramAPI(id={id(self)})"

    def __init__(self, token=None, api_url=None, proxy_url=None):
        TelegramAPI.token = token
        TelegramAPI.api_url = api_url
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
        TelegramAPI.client_args = {
            "timeout": timeout,
            "proxies": proxy_url,
            "limits": limits,
        }
        TelegramAPI.client = httpx.AsyncClient(**self.client_args)

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    @classmethod
    async def construct(cls):
        cls.client = httpx.AsyncClient(**cls.client_args)
        cls.getMe()
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
    ) -> Tuple[int, bytes]:
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

        return res.status_code, (json.loads(res.content))

    @classmethod
    async def is_ok(cls, res: Tuple[int, dict]) -> bool:
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
    ) -> dict:

        url = f"{cls.api_url}/{method}"
        _method = "GET" if request_data is None else "POST"
        if request_data is None:
            request_data = RequestData(kwargs)
        if isinstance(request_data, RequestData):
            res = await cls.__req(url, _method, request_data)
        else:
            res = await cls.__req(url, _method, RequestData(request_data))
        return res

    @classmethod
    async def call_method(
        cls,
        method: str,
        **kwargs
    ) -> dict:
        return await cls.is_ok(
            await cls.__method(
                method,
                **kwargs
            )
        )

    @classmethod
    async def getMe(cls) -> dict:
        if cls.me is None:
            cls.me = await cls.is_ok(await cls.__method("getMe"))
        return cls.me

    @classmethod
    async def getUpdates(
        cls,
        offset: Optional[int] = 0,
        limit: Optional[int] = 100,
        timeout: Optional[int] = 5,
        allowed_updates: Optional[List[str]] = None
    ) -> List["Types.Update"]:
        if allowed_updates is None:
            allowed_updates = cls.update_types

        TelegramAPI.update_types = allowed_updates

        return await cls.is_ok(
            await cls.__method(
                "getUpdates",
                offset=offset,
                limit=limit,
                timeout=timeout,
                allowed_updates=allowed_updates,
            )
        )

    @classmethod
    async def sendMessage(
        cls,
        chat_id,
        text,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        **kwargs
    ) -> dict:
        return await cls.is_ok(
            await cls.__method(
                "sendMessage",
                chat_id=chat_id,
                text=text,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                **kwargs
            )
        )

    @classmethod
    async def sendMessage(
        cls,
        chat_id,
        text,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        **kwargs
    ) -> dict:
        return await cls.is_ok(
            await cls.__method(
                "sendMessage",
                chat_id=chat_id,
                text=text,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                **kwargs
            )
        )


class Types:
    class DefaultType:
        def __init__(self, d):
            self._d = d

        def __repr__(self) -> str:
            string = f"{self.__class__.__name__}("
            for k, v in self._d.items():
                string += f"{k}={repr(v)}, "
            return string+")"

        def __iter__(self):
            return iter(self._d)

        def __getattr__(self, __name: str) -> Any:
            return self._d[__name]

        def __getitem__(self, name):
            return self._d[name]

    class Update(DefaultType):
        @property
        def update_id(self):
            return self._d['update_id']

        @property
        def update_type(self):
            for t in TelegramAPI.update_types:
                if t in self._d:
                    return t
            return None

        @property
        def update_object(self):
            return self._d[self.update_type]

        def __repr__(self) -> str:
            string = f"[id={self.update_id}] {self.update_type}("
            for k, v in self.update_object.items():
                string += f"{k}={repr(v)}, "
            return string+")"

    class Chat(DefaultType):
        @property
        def id(self) -> int:
            return self._d['id']

    class From(DefaultType):
        @property
        def id(self) -> int:
            return self._d['id']

    class Message(DefaultType):
        @property
        def id(self) -> int:
            return self._d['message_id']

        @property
        def from_user(self):
            return Types.From(self._d['from'])

        @property
        def from_chat(self):
            return Types.Chat(self._d['chat'])

        @property
        def text(self):
            return self._d['text']

        async def reply(self, text, **kwargs):
            return await TelegramAPI.sendMessage(
                self.from_chat.id,
                text,
                reply_to_message_id=self.id,
                allow_sending_without_reply=True,
                **kwargs
            )


class Telegram:
    token = "440329606:AAFHbbkn1dyMaCq9WkoHkLFuYLkKHlXl5ss"
    api_url = f"https://api.telegram.org/bot"

    def __init__(self):
        self.running = True
        self.api = TelegramAPI(self.token, f"{self.api_url}{self.token}")
        self.loop = asyncio.new_event_loop()
        self.handlers = {}
        self.handlers_types = {}

    def __aenter__(self):
        return self

    def __non_async__(self, func, data):
        asyncio.run_coroutine_threadsafe(func(data), self.loop)

    async def __start(self, offset=0):
        while self.running:
            await asyncio.sleep(0.01)
            updates = await self.api.getUpdates(offset=offset)
            for update in updates:
                update = Types.Update(update)
                offset = update.update_id + 1
                if update.update_type in self.handlers:
                    try:
                        if update.update_type in self.handlers_types:
                            up = self.handlers_types[
                                update.update_type
                            ](
                                update.update_object
                            )
                        else:
                            up = Types.DefaultType(update.update_object)

                        ThreadPy.create_and_start_thread(
                            name=f"{update.update_id}-Thread",
                            target=self.__non_async__,
                            args=(
                                self.handlers[update.update_type],
                                up,
                            )
                        )
                    except Exception as err:
                        print(err)

    def set_handler(self, type: str, handler: Callable, typeClass=None):
        self.handlers[type] = handler
        self.handlers_types[type] = typeClass
        return self

    def start(self):
        self.loop.run_until_complete(self.__start())
