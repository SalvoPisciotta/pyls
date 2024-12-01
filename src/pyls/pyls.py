from pyls.ls import PyLS
from pyls.parser import PyLSParser
import json


def main():
    json_input = "structure.json"
    parser = PyLSParser()
    args = parser.args

    with open(json_input) as f:
        json_structure = json.load(f)

    ls = PyLS(json_structure=json_structure, options=args)

    ls.generate_output()

    print(ls.get_output())


if __name__ == "__main__":
    main()
