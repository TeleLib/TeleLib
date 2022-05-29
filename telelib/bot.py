import requests


class Bot:
    def __init__(self, token, url="https://api.telegram.org/", timeout=5, proxy=None):
        self.__timeout = timeout
        self.__proxy = proxy
        self.__request = requests.Session()
        self.__request.headers = {
            "User-Agent": "TeleLib/6.0 (Python)",
        }
        self.__token = token
        self.__url = url
        self.__r_url = f"{url}bot{token}/"

        self.__threads = []
        self.__status = "stopped"

    def start(self):
        self.__status = "running"

    def stop(self):
        self.__status = "stopped"

    def __enter__(self):
        self.start()
        return self

    def __del__(self):
        self.stop()
        return None
