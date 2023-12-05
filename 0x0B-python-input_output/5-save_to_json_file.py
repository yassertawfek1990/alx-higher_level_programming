#!/usr/bin/python3
"""define dd"""
import json


def save_to_json_file(my_obj, filename):
    """adsk klak"""
    j = json.dumps(my_obj)
    with open(filename, 'w') as q:
        return q.write(j)

