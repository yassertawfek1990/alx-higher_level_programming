#!/usr/bin/python3
"""Seesponse."""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    url = argv[1]

    s = get(url)
    X = 'Error code: {}'
    t = response.status_code
    print(X.format(t) if (t >= 400) else s.text)
