from telelib import TeleLib

if __name__ == "__main__":
    TeleLib = TeleLib(open("TOKEN").read().strip())

    TeleLib.Bot.start()
