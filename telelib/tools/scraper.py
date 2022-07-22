
import json
import telelib
import re
import string

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class Scraper:
    def __repr__(self) -> str:
        return (f"Telegram Document Scraper v{telelib.__VERSION__}")

    def __init__(self):
        self.METHODS = "methods"
        self.TYPES = "types"

    def __get(self, url: str) -> dict:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features="html5lib")
        dev_rules = soup.find("div", {"id": "dev_page_content"})
        curr_type = ""
        curr_name = ""

        items = {
            self.METHODS: dict(),
            self.TYPES: dict(),
        }

        for x in list(dev_rules.children):
            if x.name == "h3" or x.name == "hr":
                curr_name = ""
                curr_type = ""

            if x.name == "h4":
                anchor = x.find("a")
                name = anchor.get("name")
                if name and "-" in name:
                    curr_name = ""
                    curr_type = ""
                    continue

                curr_name, curr_type = self.__type_name(x, anchor, items, url)

            if not curr_type or not curr_name:
                continue

            if x.name == "p":
                items[curr_type][curr_name].setdefault(
                    "description", []).extend(clean_tg_description(x, url))

            if x.name == "table":
                get_fields(curr_name, curr_type, x, items, url)

            if x.name == "ul":
                get_subtypes(curr_name, curr_type, x, items, url)

            if curr_type == METHODS and \
                    items[curr_type][curr_name].get("description"):
                get_method_return_type(
                    curr_name, curr_type,
                    items[curr_type][curr_name].get("description"),
                    items
                )

        return items

    def __type_name(self, t: Tag, anchor: Tag, items: dict, url: str):
        if t.text[0].isupper():
            curr_type = self.TYPES
        else:
            curr_type = self.METHODS
        curr_name = t.get_text()
        items[curr_type][curr_name] = {"name": curr_name}

        href = anchor.get("href")
        if href:
            items[curr_type][curr_name]["href"] = url + href

        return curr_name, curr_type

    def run(self, filename):
        print("parsing", telelib.TeleLib.Tools.documents_path)
        items = self.__get(telelib.TeleLib.Tools.documents_path)
        if verify_type_parameters(items) or verify_method_parameters(items):
            raise RuntimeError("Failed to validate schema.")

        file_name = telelib.main_path + "/generated/" + filename

        with open(f"{filename}.json", "w") as f:
            json.dump(items, f, indent=4)

        with open(f"{filename}.min.json", "w") as f:
            json.dump(items, f)
