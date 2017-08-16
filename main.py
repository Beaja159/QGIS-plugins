# -*- coding: utf-8 -*-

import json


def main():
    with open('in.json', encoding='utf-8') as fin:
        data = json.loads(fin.read().encode("utf-8"))

    for feature in data['features']:
        feature['properties']['comments'] = []
        feature['properties']['responses'] = [
            {
                'input': '1-tytu',
                'value': feature['properties']['1-tytu']
            },
            {
                'input': '2-opis',
                'value': feature['properties']['2-opis']
            },
            {
                'input': '3-symbol',
                'value': [feature['properties']['3-symbol']]
            },
        ]
        del feature['properties']['1-tytu']
        del feature['properties']['2-opis']
        del feature['properties']['3-symbol']

    with open('out.json', 'w', encoding='utf-8') as fout:
        json.dump(data, fout)


if __name__ == '__main__':
    main()
