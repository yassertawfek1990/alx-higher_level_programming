#!/usr/bin/python3
""" dg d"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    p = argv[1]
    w = argv[2]
    x = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(w, p)

    s = get(URL)
    json = s.json()

    for e in json:
        if x > 9:
            break
        h = e.get('sha')
        au = e.get('commit').get('author').get('name')
        print("{}: {}".format(h, au))
        x += 1
