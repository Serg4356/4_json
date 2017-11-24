import json
from urllib import request


def load_data(filepath):
    page = request.urlopen(filepath)
    lines = []
    for line in page.readlines():
        lines.append(line)
    page.close()
    for i in range(len(lines)):
        lines[i] = lines[i].decode('utf-8')
    data = ''.join(lines)
    return data


def pretty_print_json(data):
    jdata = json.loads(data)
    return json.dumps(jdata, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    print(pretty_print_json(load_data('https://devman.org/media/filer_public/1d/32/1d32132e-efa4-4a6c-bd32-312acc3710ad/alco_shops.json')))