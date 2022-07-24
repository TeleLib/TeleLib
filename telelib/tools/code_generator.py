

import json
import os
import telelib
from textwrap import wrap


class CodeGenerator:
    def __init__(self):
        self.Scheme = None

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

        dir_path = telelib.main_path + "/generated/" \
            + "python-generated-types/"

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        all_classes = [
            "from typing import List",
            "from telelib.bot import DefaultType",
            self._gen_core_types(),
        ]

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
    # \"\"\" Summery

    # Links
    # ----------
    # @url \"\"\"
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
                    doc_string = f'"""{d}\n\nReturns:\n-----\n{t} \n"""'
                    doc_string = ""
                    props.append(
                        f"\n\n\n\n\n\t@property"
                        f"\n\tdef {_safe_name}(self) -> {t}:"
                        f"\n\t{doc_string}"
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
            all_classes.append(class_generated)

            print(f"generated {name}")

        formatted_classes = self._format_code("\n\n".join(all_classes))

        with open(f"{dir_path}all-types.py", "w") as file:
            file.write(formatted_classes)

            print(f"written at {dir_path}all-types.py")

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

        dir_path = telelib.main_path + "/generated/" \
            + "python-generated-methods/"

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        all_classes = [
            "from typing import List",
            "from telelib.bot import DefaultMethod",
        ]

        for _, d in self.Scheme['methods'].items():
            class_generated = type_stub
            name = d["name"]
            href = d["href"]
            description = d["description"]

            class_generated = class_generated.replace('TypeName', name)
            class_generated = class_generated.replace(
                'Summery',
                f"# @url {href}"
                f"\n#"
                + (f"\n# ".join(wrap(", ".join(description), 60)))
            )

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
                        props.append(
                            f"{_safe_name}: {t},"
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

            all_classes.append(class_generated)

            print(f"generated {name}")

        formatted_classes = self._format_code("\n\n".join(all_classes))

        with open(f"{dir_path}all-methods.py", "w") as file:
            file.write(formatted_classes)

            print(f"written at {dir_path}all-methods.py")

    def _format_code(self, code):
        import autopep8
        return autopep8.fix_code(code)

    def run(
        self,
        filename
    ):
        file_name = telelib.main_path + "/generated/" + filename
        self.Scheme = json.load(open(file_name, "r"))
        print("Successfully loaded Scheme from " + file_name)

        self._gen_types()
        self._gen_methods()
