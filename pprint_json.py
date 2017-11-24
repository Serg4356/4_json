import json
import sys


def load_data(filepath):
    data = open(filepath,'r').read()
    return data


def pretty_print_json(data):
    jdata = json.loads(data)
    return json.dumps(jdata, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    print(pretty_print_json(load_data(sys.argv[1])))