#!/usr/bin/python3
""" dv """


if __name__ == '__main__':
    import sys
    from urllib import request, error

    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as s:
            print(s.read().decode('utf-8'))
    except error.HTTPError as r:
        print("Error code: {}".format(r.status))
