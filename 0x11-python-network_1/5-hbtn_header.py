#!/usr/bin/python3
""" erv """

if __name__ == '__main__':
    from requests import get
    from sys import argv

    e = get(argv[1])
    print(e.headers.get('X-Request-Id'))
