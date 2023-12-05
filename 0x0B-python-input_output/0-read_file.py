#!/usr/bin/python3
"""Defines dad"""


def read_file(filename=""):
    """returns fsfdf"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
