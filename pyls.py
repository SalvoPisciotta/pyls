from src.ls import PyLS
from src.parser import get_parser, check_args
import json

json_input = "structure.json"

parser = get_parser()

args = parser.parse_args()

check_args(args)

with open(json_input) as f:
    json_structure = json.load(f)

ls = PyLS(json_structure= json_structure, options = args)

ls.generate_output()
print(ls.get_output())
