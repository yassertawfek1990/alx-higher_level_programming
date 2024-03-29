#!/usr/bin/python3
"""Sendsponse."""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    a = {'q': argv[1] if len(argv) >= 2 else ""}
    s = post(URL, a)

    y = s.headers['content-type']

    if y == 'application/json':
        ll = s.json()
        _i = ll.get('id')
        m = ll.get('name')
        if (ll != {} and _i and m):
            print("[{}] {}".format(_i, m))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
