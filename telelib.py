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
        if msg.text == "hello":
            await TeleLib.tg(
                res := telegram.sendMessage(
                    text="Hello : )",
                    chat_id=msg.chat.id
                )
            )
            print(res.result())

    telelib.Bot.set_event_handler('main', main)
    telelib.Bot.set_event_handler(telegram.Message, message)

    telelib.start()
    # telelib.Tools.CodeGeneratorRun()
