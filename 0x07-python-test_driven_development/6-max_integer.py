#!/usr/bin/python3
"""Modul"""


def max_integer(list=[]):
    """Functionto"""
    if len(list) == 0:
        return None
    r = list[0]
    x = 1
    while x < len(list):
        if list[x] > r:
            r = list[x]
        x += 1
    return r
