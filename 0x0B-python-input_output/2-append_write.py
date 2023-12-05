#!/usr/bin/python3
"""define dd"""


def append_write(filename="", text=""):
    """advs sF"""
    with open(filename, 'a', encoding="UTF8") as q:
        return q.write(text)
