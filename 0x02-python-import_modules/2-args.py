#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif len(argv) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i in range (len(sys.argv) - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
