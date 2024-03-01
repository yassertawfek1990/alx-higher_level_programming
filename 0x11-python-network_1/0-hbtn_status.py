#!/usr/bin/python3
"""F"""
import urllib.request


if __name__ == "__main__":
    q = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(q) as s:
        d = s.read()
        print("Body response:")
        print("\t- type: {}".format(type(d)))
        print("\t- content: {}".format(d))
        print("\t- utf8 content: {}".format(d.decode("utf-8")))
