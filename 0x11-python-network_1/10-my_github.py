#!/usr/bin/python3
""" d """

if __name__ == '__main__':
    from requests import get
    from sys import argv

    ser = argv[1]
    ss = argv[2]

    URL = "https://api.github.com/user"
    s = get(URL, auth=(ser, ss))
    json = s.json()

    print(json.get('id'))
