#!/usr/bin/python3
"""Seesponse."""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    url = argv[1]

    s = get(url)
    ERR_TXT = 'Error code: {}'
    t = s.status_code
    print(ERR_TXT.format(t) if (t >= 400) else s.text)
