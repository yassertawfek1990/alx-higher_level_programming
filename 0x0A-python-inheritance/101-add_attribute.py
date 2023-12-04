#!/usr/bin/python3
"""svsdvfV"""


def add_attribute(f, a, v):
    """dsfdsf"""
    if not hasattr(f, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(f, a, v)
