#!/usr/bin/python3
"""Defineunction"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text afn a file.

    Args:
        filename (str): The file.
        search_string (str): The strinhin the file.
        new_string (str): The sert.
    """
    with open(filename, 'r',  encoding='utf-8') as q:
        ll = []
        while True:
            l = q.readline()
            if l == "":
                break
            ll.append(l)
            if search_string in l:
                ll.append(new_string)
    with open(filename, "w", encoding='utf-8') as z:
        z.writelines(ll)
