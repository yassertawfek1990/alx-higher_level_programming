#!/usr/bin/python3
""" d """


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as s:
        print(s.headers["X-Request-Id"])
