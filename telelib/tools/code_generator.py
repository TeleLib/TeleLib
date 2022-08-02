

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
        self.core_types = {
            "Integer": "int",
            "String": "str",
            "Boolean": "bool",
            "Float": 'float',
        }
        self.all_classes = [
            "from typing import List, Union, Optional, Any",
            '''
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
            return self._d.get(__name, None)

        def __getitem__(self, name):
            return self._d.get(name, None)

    class DefaultMethod:
        def __init__(self, *args, **kwargs):
            self._called = False
            self._method: str = ""
            self._args = {}
            self._res = None

        def _call(self):
            return (self._method, self._args)

    @staticmethod
    def Typify(data, type_, recursive=True):
        if recursive:
            if isinstance(data, list):
                return [Types.Typify(d, type_) for d in data]

        if data is not None:
            return type_(data)

        return None
            ''',
            self._gen_core_types(),
        ]

    def _gen_core_types(self):
        generated_classes = []
        for key, value in self.core_types.copy().items():
            if key != 'Boolean':
                # Boolean is a special case since
                # it's not a type amd we can't inherit from it
                generated_classes.append(f"class {key}({value}):\n\t...")

        generated_classes.append("Boolean = bool")

        return "\n\n".join(generated_classes)

    def _gen_types(self):
        type_stub = """
class TypeName(Types.DefaultType):
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
                    if len(_types) > 1:
                        t = "Union[" + \
                            (", ".join(map(lambda x: f'"{x}"', _types))) + "]"
                    else:
                        t = (", ".join(map(lambda x: f'"{x}"', _types)))
                    if not field['required']:
                        t = f"Optional[{t}]"
                    _safe_name = str(field['name']).replace('from', 'from_')
                    d = "\n\t\t".join(wrap(field['description'], 60))
                    returnable = f"self._d.get(\"{field['name']}\", None)"
                    for i in field['types']:
                        returnable = (
                            f"Types.Typify("
                            f"\n\t\t{returnable},"
                            f"\n\t\t{i.split('Array of ')[-1]}"
                            f"\n\t)"
                        )

                    props.append(
                        f"\n\n\n\n\n\t@property"
                        f"\n\tdef {_safe_name}("
                        f"\n\tself"
                        f"\n\t)"
                        f" -> {t}:"
                        f"\n\t\treturn {returnable}"
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
class TypeName(Types.DefaultMethod):

    def __init__(
        self,
        ARGS
    ):
        super().__init__(
            INTSUPAR
        )
        self._method = "TypeName"
        self._res_type = RESULT_TYPE
        self._args = {}
        ARGS_PARSED

    def result(self, update_type=RESULT_TYPE_RES) -> RESULT_TYPE:
        if not self._called:
            raise Exception("You have to call the method first")

        return Types.Typify(self._res, update_type)

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
            super_props = []
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
                    if len(_types) > 1:
                        t = "Union[" + \
                            (", ".join(map(lambda x: f'"{x}"', _types))) + "]"
                    else:
                        t = (", ".join(map(lambda x: f'"{x}"', _types)))
                    if not field['required']:
                        t = f"Optional[{t}]"
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
                    super_props.append(_safe_name)

                class_generated = class_generated.replace(
                    'ARGS_PARSED',
                    "\n\t\t".join(props_list)
                )
                class_generated = class_generated.replace(
                    'ARGS',
                    "\n\t\t".join(props)
                )
                class_generated = class_generated.replace(
                    "INTSUPAR",
                    ",\n\t\t".join(super_props)
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
                'RESULT_TYPE_RES',
                d["returns"][0].split('Array of ')[-1]
            )
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

        with open(f"{telelib.main_path}/telelib/telegram.py", "w") as file:
            file.write(self._format_code("\n\n".join(self.all_classes)))

            print(f"written at {telelib.main_path}/telelib/telegram.py")
