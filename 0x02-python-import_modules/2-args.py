#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    t = len(sys.argv) - 1
    if t == 1:
        print("1 argument:")
    elif t == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(t))
    for i in range (t):
        print("{}: {}".format(i + 1, t[i + 1]))
