#!/usr/bin/python3
""" sf """

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    D = urllib.parse.urlencode({"email": email})
    D = D.encode('ascii')

    with urllib.request.urlopen(url, D) as s:
        print(s.read().decode('utf-8'))
