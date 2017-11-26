import json
import sys


def load_data(filepath):
    unstruckted_data = json.loads(open(filepath,'r').read())
    return unstruckted_data


def pretty_print_json(unstruckted_data):
    return json.dumps(unstruckted_data, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    print(pretty_print_json(load_data(sys.argv[1])))