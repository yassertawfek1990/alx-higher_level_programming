#!/usr/bin/python3
for f in range(9):
    for k in range(f + 1, 10):
        if f * 10 + k < 89:
            print("{:d}{:d}".format(f, k), end=", ")
print("{:d}".format(89))
