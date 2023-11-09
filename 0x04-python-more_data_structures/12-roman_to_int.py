#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) is not str):
        return 0
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    t = 0
    n = 0
    for i in reversed(roman_string):
        n = d[i]
        if t < n * 5:
            t += n
        else:
            t -= n
    return t
