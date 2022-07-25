

import json
import os
import telelib
from textwrap import wrap

"""
Python code generator for telelib.

Generates all Types and Methods as
Python Classes from the
https://core.telegram.org/bots/api documentation.
"""


class CodeGenerator:
    def __init__(self):
        self.Scheme = None
        self.all_classes = [
            "from typing import List",
            "from telelib.bot import DefaultType",
            "from telelib.bot import DefaultMethod",
            self._gen_core_types(),
        ]

    def _gen_core_types(self):
        core_types = {
            "Integer": "int",
            "String": "str",
            # "Boolean": "bool",
            "Float": 'float',
        }
        generated_classes = []
        for key, value in core_types.items():
            generated_classes.append(f"class {key}({value}):\n\t...")

        generated_classes.append("Boolean = bool")

        return "\n\n".join(generated_classes)

    def _gen_types(self):
        type_stub = """
class TypeName(DefaultType):
    Props
"""
        for _, d in self.Scheme['types'].items():
            class_generated = type_stub
            name = d["name"]
            href = d["href"]
            description = d["description"]

            class_generated = class_generated.replace('TypeName', name)
            class_generated = class_generated.replace(
                'Summery', f"\n\t".join(wrap(", ".join(description), 60))
            )
            class_generated = class_generated.replace(
                '@url', href
            )
            props = []
            if "fields" in d:
                for field in d["fields"]:
                    _types = []
                    for i in field['types']:
                        if "Array of Array of " in i:
                            i = f"List[List[{i.split('Array of ')[-1]}]]"
                        if "Array of" in i:
                            i = f"List[{i.split('Array of ')[-1]}]"
                        _types.append(i)
                    if not field['required']:
                        _types.append("None")
                    t = "|".join(map(lambda x: f'"{x}"', _types))
                    _safe_name = str(field['name']).replace('from', 'from_')
                    d = "\n\t\t".join(wrap(field['description'], 60))
                    props.append(
                        f"\n\n\n\n\n\t@property"
                        f"\n\tdef {_safe_name}("
                        f"\n\tself"
                        f"\n\t)"
                        f" -> {t}:"
                        f"\n\t\treturn self._d[\"{field['name']}\"]"
                    )

                class_generated = class_generated.replace(
                    'Props',
                    "".join(props)
                )
            else:
                class_generated = class_generated.replace(
                    'Props',
                    "..."
                )
            self.all_classes.append(class_generated)

            print(f"generated {name}")

    def _gen_methods(self):
        type_stub = """
Summery
class TypeName(DefaultMethod):

    def __init__(
        self,
        ARGS
    ):
        self._method = "TypeName"
        self._res_type = RESULT_TYPE
        self._args = {}
        ARGS_PARSED

    def result(self) -> RESULT_TYPE:
        if not self._called:
            raise Exception("You have to call the method first")

        return self._res

"""

        for _, d in self.Scheme['methods'].items():
            class_generated = type_stub
            name = d["name"]
            # href = d["href"]
            # description = d["description"]

            class_generated = class_generated.replace('TypeName', name)
            class_generated = class_generated.replace(
                'Summery',
                ""
            )
            # class_generated = class_generated.replace(
            #     'Summery',
            #     f"# @url {href}"
            #     f"\n#"
            #     + (f"\n# ".join(wrap(", ".join(description), 60)))
            # )

            props = []
            props_list = []
            if "fields" in d:
                for field in d["fields"]:
                    _types = []
                    for i in field['types']:
                        if "Array of Array of " in i:
                            i = f"List[List[{i.split('Array of ')[-1]}]]"
                        if "Array of" in i:
                            i = f"List[{i.split('Array of ')[-1]}]"
                        _types.append(i)
                    t = "|".join(map(lambda x: f'"{x}"', _types))
                    _safe_name = str(field['name']).replace('from', 'from_')
                    if field['required']:
                        props.insert(
                            0, f"{_safe_name}: {t},"
                        )
                    else:
                        props.append(
                            f"{_safe_name}: {t} = None,"
                        )
                    props_list.append(
                        f"self._args['{field['name']}'] = {_safe_name}")

                class_generated = class_generated.replace(
                    'ARGS_PARSED',
                    "\n\t\t".join(props_list)
                )
                class_generated = class_generated.replace(
                    'ARGS',
                    "\n\t\t".join(props)
                )

            else:
                class_generated = class_generated.replace(
                    'ARGS_PARSED',
                    ""
                )
                class_generated = class_generated.replace(
                    'ARGS',
                    ""
                )

            res_type = d["returns"][0]
            if "Array of Array of " in res_type:
                res_type = f"List[List[{res_type.split('Array of ')[-1]}]]"
            if "Array of" in res_type:
                res_type = f"List[{res_type.split('Array of ')[-1]}]"

            class_generated = class_generated.replace(
                'RESULT_TYPE',
                f'"{res_type}"'
            )

            self.all_classes.append(class_generated)

            print(f"generated {name}")

    def _format_code(self, code):
        import autopep8
        return autopep8.fix_code(code)

    def run(
        self,
        filename
    ):
        telelib.TeleLib.Tools.ScraperRun()
        file_name = telelib.main_path + "/generated/" + filename
        self.Scheme = json.load(open(file_name, "r"))
        print("Successfully loaded Scheme from " + file_name)

        self._gen_types()
        self._gen_methods()

        dir_path = telelib.main_path + "/generated/"

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        with open(f"{dir_path}telegram.py", "w") as file:
            file.write(self._format_code("\n\n".join(self.all_classes)))

            print(f"written at {dir_path}telegram.py")
