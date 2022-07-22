import json
import os

api = json.load(open('api.json', 'r'))

type_stub = """
from telelib.bot import DefaultType

Summery
class TypeName(DefaultType):

    Props

"""

dir_path = "./pygen/"
# os.mkdir(dir_path)

for _, d in api['types'].items():
    class_generated = type_stub
    name = d["name"]
    href = d["href"]
    description = d["description"]

    class_generated = class_generated.replace('TypeName', name)
    class_generated = class_generated.replace(
        'Summery',
        f"# @url {href}"
        f"# {description}"
    )

    props = []
    if "fields" in d:
        for field in d["fields"]:
            t = "|".join(field['types'])
            props.append(
                f"\n\t# @var {field['name']} {field['description']}\n"
                f"\t@property\n\tdef {field['name']}(self) -> {t}:\n\t\treturn self._d[\"{field['name']}\"]"
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

    with open(f"{dir_path}{name}.py", "w") as file:
        file.write(class_generated)

    print(f"generated {name}")
