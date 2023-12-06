#!/usr/bin/python3
"""Defineunction."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text afn a file.

    Args:
        filename (str): The file.
        search_string (str): The strinhin the file.
        new_string (str): The sert.
    """
    xt = ""

    with open(filename) as q:
        for l in q:
            xt += l
            if search_string in l:
                xt += new_string
    with open(filename, "w") as z:
        z.write(xt)
