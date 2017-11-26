import json
import sys


def load_data(filepath):
    with open(filepath,'r') as opened_file:
        unstruckted_data = json.loads(opened_file.read())
    return unstruckted_data


def prettify_json(unstruckted_data):
    return json.dumps(unstruckted_data, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    print(prettify_json(load_data(sys.argv[1])))