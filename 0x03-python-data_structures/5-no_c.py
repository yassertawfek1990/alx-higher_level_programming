#!/usr/bin/python3
def no_c(my_string):
    n = ""
    for x in my_string:
        if x != "c" and x != "C":
            n += x
    return n
