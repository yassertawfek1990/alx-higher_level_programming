#!/usr/bin/python3
"""define dd"""


def append_after(filename="", search_string="", new_string=""):
    """Insert te"""
    xt = ""

    with open(filename) as q:
        for l in q:
            xt += l
            if search_string in l:
                xt += new_string

    with open(filename, "w") as z:
        z.write(xt)
