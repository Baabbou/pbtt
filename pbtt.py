from argparse import ArgumentParser
from urllib.parse import urlparse
from sys import exit
import xmltodict
import json


parser = ArgumentParser(description="Post Body Translator Tool: A tool to translate post body into XML and Json")
parser.add_argument("value", help="The body you need to translate")
parser.add_argument("-j", "--json", help="The given input is in Json", action="store_true")
parser.add_argument("-x", "--xml", help="The given input is in XML", action="store_true")
parser.add_argument("-t", "--tldr", help="example: pbtt '?blabla=truc&machin=test'", action="store_true")

args = parser.parse_args()


def json_string(args: dict) -> str:
    output = "?"
    for key, val in args.items():
        output += f"{key}={val}&"
    return output[:-1]


def string_json(input: str) -> str:
    if not input[0] == "?":
        input = f"?{input}"
    args = urlparse(input).query.split("&")

    output = {}
    for arg in args:
        key, value = arg.split("=")
        output[key] = value
    output = json.dumps(output)
    return output


def string_xml(input: str) -> str:
    if not input[0] == "?":
        input = f"?{input}"
    args = urlparse(input).query.split("&")

    output = '<?xml version="1.0" encoding="UTF-8"?>'
    for arg in args:
        key, value = arg.split("=")
        output += f"<{key}>{value}</{key}>"
    return output
    

if __name__ == '__main__':
    
    input = args.value
    output1 = ""
    output2 = ""

    try:
        if args.json:
            input = json.loads(input.replace("'", '"'))
            output1 = json_string(input)
            output2 = string_xml(output1)
        elif args.xml:
            input = input.replace('<?xml version="1.0" encoding="UTF-8"?>', "")
            input = f"<root>{input}</root>"
            dict_input = xmltodict.parse(input).get("root")
            output1 = json_string(dict_input)
            output2 = str(dict_input).replace("'", '"')
        else:
            output1 = string_json(input)
            output2 = string_xml(input)
    except Exception as e:
        print("Error: Did you precise the right data type ?")
        exit(1)
    
    print(output1)
    print(output2)
