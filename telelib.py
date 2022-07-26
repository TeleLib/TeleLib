import asyncio
from telelib import TeleLib, telegram

if __name__ == "__main__":
    telelib = TeleLib(open("TOKEN").read().strip())

    async def main():
        # await TeleLib.tg(
        #     res := telegram.sendMessage(text="Hello", chat_id=400610322)
        # )

        # print(res.result())
        ...

    async def message(msg: telegram.Message):
        print(msg)
        print(msg.text)
        if msg.text == "Hello":
            await TeleLib.tg(
                res := telegram.sendMessage(text="Hello", chat_id=400610322)
            )

    telelib.Bot.event_handlers['main'] = main
    telelib.Bot.set_event_handler(telegram.Message, message)

    telelib.start()
    # telelib.Tools.CodeGeneratorRun()
