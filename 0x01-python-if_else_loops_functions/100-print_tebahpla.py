#!/usr/bin/python3
for f in range(122, 96, -1):
    if f % 2:
        f = f - 32
    print("{:c}".format(f), end="")
