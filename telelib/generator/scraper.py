# using https://github.com/PaulSonOfLars/telegram-bot-api-spec
# with a little bit of improvements of course :)
import json
import re
import string

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from telelib import generator_path

TG_CORE_TYPES = ["String", "Boolean", "Integer", "Float"]
ROOT_URL = "https://core.telegram.org"
TO_SCRAPE = {
    "api": ROOT_URL + "/bots/api",
}

METHODS = "methods"
TYPES = "types"

APPROVED_NO_SUBTYPES = {
    "InputFile"
}
APPROVED_MULTI_RETURNS = [
    ['Message', 'Boolean']
]


def get_subtypes(curr_name: str, curr_type: str, x: Tag, items: dict, url: str):
    if curr_name == "InputFile":
        return

    list_contents = []
    for li in x.find_all("li"):
        list_contents.extend(clean_tg_description(li, url))

    if curr_type == TYPES:
        items[curr_type][curr_name]["subtypes"] = list_contents

    items[curr_type][curr_name]["description"] += [
        f"- {s}" for s in list_contents]


def get_fields(curr_name: str, curr_type: str, x: Tag, items: dict, url: str):
    body = x.find("tbody")
    fields = []
    for tr in body.find_all("tr"):
        children = list(tr.find_all("td"))
        if curr_type == TYPES and len(children) == 3:
            desc = clean_tg_field_description(children[2], url)
            fields.append(
                {
                    "name": children[0].get_text(),
                    "types": clean_tg_type(children[1].get_text()),
                    "required": not desc.startswith("Optional. "),
                    "description": desc,
                }
            )

        elif curr_type == METHODS and len(children) == 4:
            fields.append(
                {
                    "name": children[0].get_text(),
                    "types": clean_tg_type(children[1].get_text()),
                    "required": children[2].get_text() == "Yes",
                    "description": clean_tg_field_description(children[3], url)
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


def get_method_return_type(curr_name: str, curr_type: str,
                           description_items: list[str], items: dict):
    description = "\n".join(description_items)
    ret_search = re.search(
        "(?:on success,|returns)([^.]*)(?:on success)?",
        description, re.IGNORECASE)
    ret_search2 = re.search("([^.]*)(?:is returned)",
                            description, re.IGNORECASE)
    if ret_search:
        extract_return_type(curr_type, curr_name,
                            ret_search.group(1).strip(), items)
    elif ret_search2:
        extract_return_type(curr_type, curr_name,
                            ret_search2.group(1).strip(), items)


def extract_return_type(curr_type: str,
                        curr_name: str, ret_str: str, items: dict):
    array_match = re.search(r"(?:array of )+(\w*)", ret_str, re.IGNORECASE)
    if array_match:
        ret = clean_tg_type(array_match.group(1))
        rets = [f"Array of {r}" for r in ret]
        items[curr_type][curr_name]["returns"] = rets
    else:
        words = ret_str.split()
        rets = [
            r for ret in words
            for r in clean_tg_type(ret.translate(str.maketrans("", "", string.punctuation)))
            if ret[0].isupper()
        ]
        items[curr_type][curr_name]["returns"] = rets


def clean_tg_field_description(t: Tag, url: str) -> str:
    return " ".join(clean_tg_description(t, url))


def clean_tg_description(t: Tag, url: str) -> list[str]:
    # Replace HTML emoji images with actual emoji
    for i in t.find_all("img"):
        i.replace_with(i.get("alt"))

    # Make sure to include linebreaks, or spacing gets weird
    for br in t.find_all("br"):
        br.replace_with("\n")

    # Replace helpful anchors with the actual URL.
    for a in t.find_all("a"):
        anchor_text = a.get_text()
        if "»" not in anchor_text:
            continue

        link = a.get("href")
        # Page-relative URL
        if link.startswith("#"):
            link = url + link
        # Domain-relative URL
        elif link.startswith("/"):
            link = ROOT_URL + link

        anchor_text = anchor_text.replace(" »", ": " + link)
        a.replace_with(anchor_text)

    text = t.get_text()

    # Replace any weird double whitespaces (eg double space, newlines, tabs) with single occurrences
    text = re.sub(r"(\s){2,}", r"\1", text)

    # Replace weird UTF-8 quotes with proper quotes
    text = text.replace('”', '"').replace('“', '"')

    # Replace weird unicode ellipsis with three dots
    text = text.replace("…", "...")

    # Use sensible dashes
    text = text.replace(u"\u2013", "-")
    text = text.replace(u"\u2014", "-")
    # Use sensible single quotes
    text = text.replace(u"\u2019", "'")

    # Split on newlines to improve description output.
    return [t.strip() for t in text.split("\n") if t.strip()]


def get_proper_type(t: str) -> str:
    if t == "Messages":  # Avoids https://core.telegram.org/bots/api#sendmediagroup
        return "Message"

    elif t == "Float number":
        return "Float"

    elif t == "Int":
        return "Integer"

    elif t == "True" or t == "Bool":
        return "Boolean"

    return t


def clean_tg_type(t: str) -> list[str]:
    pref = ""
    if t.startswith("Array of "):
        pref = "Array of "
        t = t[len("Array of "):]

    # Fix situations like "A or B"
    fixed_ors = [x.strip() for x in t.split(" or ")]
    fixed_ands = [x.strip() for fo in fixed_ors for x in fo.split(
        " and ")]  # Fix situations like "A and B"
    # Fix situations like "A, B"
    fixed_commas = [x.strip() for fa in fixed_ands for x in fa.split(", ")]
    return [pref + get_proper_type(x) for x in fixed_commas]


# Returns True if an issue is found.
def verify_type_parameters(items: dict) -> bool:
    issue_found = False

    for type_name, values in items[TYPES].items():
        # check all values have a URL
        if not values.get("href"):
            print(f"{type_name} has no link!")
            issue_found = True
            continue

        fields = values.get("fields", [])
        if len(fields) == 0:
            subtypes = values.get("subtypes", [])
            description = "".join(values.get("description", [])).lower()
            # Some types are abstract and have no information or subtypes - this is mentioned in their description.
            # Otherwise, check if they're manually approved.
            if not subtypes and \
                    not ("currently holds no information" in description or type_name in APPROVED_NO_SUBTYPES):
                print("TYPE", type_name,
                      "has no fields or subtypes, and is not approved")
                issue_found = True
                continue

            for st in subtypes:
                if st in items[TYPES]:
                    items[TYPES][st].setdefault(
                        "subtype_of", []).append(type_name)
                else:
                    print("TYPE", type_name, "USES INVALID SUBTYPE", st)
                    issue_found = True

        # check all parameter types are valid
        for param in fields:
            field_types = param.get("types")
            for field_type_name in field_types:
                while field_type_name.startswith("Array of "):
                    field_type_name = field_type_name[len("Array of "):]

                if field_type_name not in items[TYPES] and field_type_name not in TG_CORE_TYPES:
                    print("UNKNOWN FIELD TYPE", field_type_name)
                    issue_found = True

    return issue_found


# Returns True if an issue is found.
def verify_method_parameters(items: dict) -> bool:
    issue_found = False
    # Type check all methods
    for method, values in items[METHODS].items():
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
        if len(returns) > 1 and returns not in APPROVED_MULTI_RETURNS:
            print(f"{method} has multiple return types: {returns}")

        # check all parameter types are valid
        for param in values.get("fields", []):
            types = param.get("types")
            for t in types:
                while t.startswith("Array of "):
                    t = t[len("Array of "):]

                if t not in items[TYPES] and t not in TG_CORE_TYPES:
                    issue_found = True
                    print("UNKNOWN PARAM TYPE", t)

        # check all return types are valid
        for ret in values.get("returns", []):
            while ret.startswith("Array of "):
                ret = ret[len("Array of "):]

            if ret not in items[TYPES] and ret not in TG_CORE_TYPES:
                issue_found = True
                print("UNKNOWN RETURN TYPE", ret)

    return issue_found
