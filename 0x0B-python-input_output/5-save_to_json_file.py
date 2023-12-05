#!/usr/bin/python3
"""define dd"""
import json


def save_to_json_file(my_obj, filename):
    """adsk klak"""
    with open(filename, "w") as q:
        json.dump(my_obj, q)

