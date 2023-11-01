#!/usr/bin/python3
def uppercase(str):
    for f in str:
        if ord("a") <= ord(f) <= ord("z"):
            f = chr(ord(f) - 32)
        print("{:s}".format(f), end="")
    print()
