#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    t = len(sys.argv) - 1
    if t == 0:
        print("0 arguments.")
    elif t == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(t))
    for i in range (t):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
