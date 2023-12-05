#!/usr/bin/python3
"""define dd"""
import json


def load_from_json_file(filename):
    """ada sd"""
    with open(filename, 'r') as q:
        return json.load(q)
