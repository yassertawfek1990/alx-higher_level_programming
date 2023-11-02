#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in [+, -, *, /]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = sys.argv[1]
    op = sys.argv[2]
    b = sys.argv[3]
    if op == +:
        print("{} + {} = {}".format(a, b, add(a, b)))
    if op == -:
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if op == *:
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if op == /:
        print("{} / {} = {}".format(a, b, div(a, b)))
