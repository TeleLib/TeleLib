import json
import telelib
import re
import string

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


# i used  https://github.com/PaulSonOfLars/telegram-bot-api-spec
# as a base for this scraper
class Scraper:
    def __repr__(self) -> str:
        return f"Telegram Document Scraper v{telelib.__VERSION__}"

    def __init__(self):
        self.METHODS = "methods"
        self.TYPES = "types"
        self.TG_CORE_TYPES = ["String", "Boolean", "Integer", "Float"]

        self.APPROVED_NO_SUBTYPES = {"InputFile"}
        self.APPROVED_MULTI_RETURNS = [["Message", "Boolean"]]

    def __get_fields(
        self,
        curr_name: str,
        curr_type: str,
        x: Tag,
        items: dict,
        url: str
    ):
        body = x.find("tbody")
        fields = []
        for tr in body.find_all("tr"):
            children = list(tr.find_all("td"))
            if curr_type == self.TYPES and len(children) == 3:
                desc = self.__clean_tg_field_description(children[2], url)
                fields.append(
                    {
                        "name": children[0].get_text(),
                        "types": self.__clean_tg_type(children[1].get_text()),
                        "required": not desc.startswith("Optional. "),
                        "description": desc,
                    }
                )

            elif curr_type == self.METHODS and len(children) == 4:
                fields.append(
                    {
                        "name": children[0].get_text(),
                        "types": self.__clean_tg_type(children[1].get_text()),
                        "required": children[2].get_text() == "Yes",
                        "description": self.__clean_tg_field_description(
                            children[3], url
                        ),
                    }
                )

            else:
                print("An unexpected state has occurred!")
                print("Type:", curr_type)
                print("Name:", curr_name)
                print("Number of children:", len(children))
                print(children)
                exit(1)

        items[curr_type][curr_name]["fields"] = fields

    def __get_method_return_type(
        self,
        curr_name: str,
        curr_type: str,
        description_items: list[str],
        items: dict,
    ):
        description = "\n".join(description_items)
        ret_search = re.search(
            "(?:on success,|returns)([^.]*)(?:on success)?",
            description,
            re.IGNORECASE,
        )
        ret_search2 = re.search(
            "([^.]*)(?:is returned)", description, re.IGNORECASE
        )
        if ret_search:
            self.__extract_return_type(
                curr_type, curr_name, ret_search.group(1).strip(), items
            )
        elif ret_search2:
            self.__extract_return_type(
                curr_type, curr_name, ret_search2.group(1).strip(), items
            )

    def __extract_return_type(
        self,
        curr_type: str,
        curr_name: str,
        ret_str: str,
        items: dict
    ):
        array_match = re.search(r"(?:array of )+(\w*)", ret_str, re.IGNORECASE)
        if array_match:
            ret = self.__clean_tg_type(array_match.group(1))
            rets = [f"Array of {r}" for r in ret]
            items[curr_type][curr_name]["returns"] = rets
        else:
            words = ret_str.split()
            rets = [
                r
                for ret in words
                for r in self.__clean_tg_type(
                    ret.translate(str.maketrans("", "", string.punctuation))
                )
                if ret[0].isupper()
            ]
            items[curr_type][curr_name]["returns"] = rets

    def __clean_tg_field_description(
        self,
        t: Tag,
        url: str
    ) -> str:
        return " ".join(self.__clean_tg_description(t, url))

    def __clean_tg_description(
        self,
        t: Tag,
        url: str
    ) -> list[str]:
        for i in t.find_all("img"):
            i.replace_with(i.get("alt"))

        for br in t.find_all("br"):
            br.replace_with("\n")

        for a in t.find_all("a"):
            anchor_text = a.get_text()
            if "»" not in anchor_text:
                continue

            link = a.get("href")

            if link.startswith("#"):
                link = url + link

            elif link.startswith("/"):
                link = telelib.TeleLib.Tools.documents_path + link

            anchor_text = anchor_text.replace(" »", ": " + link)
            a.replace_with(anchor_text)

        text = t.get_text()

        text = re.sub(r"(\s){2,}", r"\1", text)
        text = text.replace("”", '"').replace("“", '"')
        text = text.replace("…", "...")
        text = text.replace("\u2013", "-")
        text = text.replace("\u2014", "-")
        text = text.replace("\u2019", "'")
        return [t.strip() for t in text.split("\n") if t.strip()]

    def __get_proper_type(
        self,
        t: str
    ) -> str:
        if t == "Messages":
            return "Message"

        elif t == "Float number":
            return "Float"

        elif t == "Int":
            return "Integer"

        elif t == "True" or t == "Bool":
            return "Boolean"

        return t

    def __clean_tg_type(
        self,
        t: str
    ) -> list[str]:
        pref = ""
        if t.startswith("Array of "):
            pref = "Array of "
            t = t[len("Array of "):]

        fixed_ors = [x.strip() for x in t.split(" or ")]
        fixed_ands = [x.strip() for fo in fixed_ors for x in fo.split(" and ")]
        fixed_commas = [x.strip() for fa in fixed_ands for x in fa.split(", ")]
        return [pref + self.__get_proper_type(x) for x in fixed_commas]

    def __get_subtypes(
        self, curr_name: str, curr_type: str, x: Tag, items: dict, url: str
    ):
        if curr_name == "InputFile":
            return

        list_contents = []
        for li in x.find_all("li"):
            list_contents.extend(self.__clean_tg_description(li, url))

        if curr_type == self.TYPES:
            items[curr_type][curr_name]["subtypes"] = list_contents

        items[curr_type][curr_name]["description"] += [
            f"- {s}" for s in list_contents
        ]

    def __get(
        self,
        url: str
    ) -> dict:
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
                    "description", []
                ).extend(self.__clean_tg_description(x, url))

            if x.name == "table":
                self.__get_fields(curr_name, curr_type, x, items, url)

            if x.name == "ul":
                self.__get_subtypes(curr_name, curr_type, x, items, url)

            if curr_type == self.METHODS and items[curr_type][curr_name].get(
                "description"
            ):
                self.__get_method_return_type(
                    curr_name,
                    curr_type,
                    items[curr_type][curr_name].get("description"),
                    items,
                )

        return items

    def __type_name(
        self,
        t: Tag,
        anchor: Tag,
        items: dict,
        url: str
    ):
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

    def __verify_types(
        self,
        items: dict
    ) -> bool:
        issue_found = False

        for type_name, values in items[self.TYPES].items():
            # check all values have a URL
            if not values.get("href"):
                print(f"{type_name} has no link!")
                issue_found = True
                continue

            fields = values.get("fields", [])
            if len(fields) == 0:
                subtypes = values.get("subtypes", [])
                description = "".join(values.get("description", [])).lower()
                # Some types are abstract and have no information
                # or subtypes - this is mentioned in their description.
                # Otherwise, check if they're manually approved.
                if not subtypes and not (
                    "currently holds no information" in description
                    or type_name in self.APPROVED_NO_SUBTYPES
                ):
                    print(
                        "TYPE",
                        type_name,
                        "has no fields or subtypes, and is not approved",
                    )
                    issue_found = True
                    continue

                for st in subtypes:
                    if st in items[self.TYPES]:
                        items[self.TYPES][st].setdefault(
                            "subtype_of", []
                        ).append(type_name)
                    else:
                        print("TYPE", type_name, "USES INVALID SUBTYPE", st)
                        issue_found = True

            # check all parameter types are valid
            for param in fields:
                field_types = param.get("types")
                for field_type_name in field_types:
                    while field_type_name.startswith("Array of "):
                        field_type_name = field_type_name[len("Array of "):]

                    if (
                        field_type_name not in items[self.TYPES]
                        and field_type_name not in self.TG_CORE_TYPES
                    ):
                        print("UNKNOWN FIELD TYPE", field_type_name)
                        issue_found = True

        return issue_found

    def __verify_methods(
        self,
        items: dict
    ) -> bool:
        issue_found = False
        # Type check all methods
        for method, values in items[self.METHODS].items():
            # check all values have a URL
            if not values.get("href"):
                print(f"{method} has no link!")
                issue_found = True
                continue

            # check all methods have a return
            returns = values.get("returns")
            if not returns:
                print(f"{method} has no return types!")
                issue_found = True
                continue

            # If we have multiple returns, this is an edge case,
            # but not a deal-breaker; check that output.
            # Some multi-returns are common and pre-approved.
            if len(returns) > 1 and returns not in self.APPROVED_MULTI_RETURNS:
                print(f"{method} has multiple return types: {returns}")

            # check all parameter types are valid
            for param in values.get("fields", []):
                types = param.get("types")
                for t in types:
                    while t.startswith("Array of "):
                        t = t[len("Array of "):]

                    if (
                        t not in items[self.TYPES]
                        and t not in self.TG_CORE_TYPES
                    ):
                        issue_found = True
                        print("UNKNOWN PARAM TYPE", t)

            # check all return types are valid
            for ret in values.get("returns", []):
                while ret.startswith("Array of "):
                    ret = ret[len("Array of "):]

                if (
                    ret not in items[self.TYPES]
                    and ret not in self.TG_CORE_TYPES
                ):
                    issue_found = True
                    print("UNKNOWN RETURN TYPE", ret)

        return issue_found

    def run(
        self,
        filename,
        indent=None
    ):
        items = self.__get(telelib.TeleLib.Tools.documents_path)
        if self.__verify_types(items) or self.__verify_methods(items):
            raise RuntimeError("Failed to validate schema.")

        file_name = telelib.main_path + "/generated/" + filename

        with open(file_name, "w") as f:
            json.dump(items, f, indent=indent)

        return "Successfully generated json Scheme at " + file_name
