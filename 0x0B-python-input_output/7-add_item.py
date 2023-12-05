#!/usr/bin/python3
"""define dd"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

l = list(sys.argv[1:])

try:
    n = load_from_json_file('add_item.json')
except Exception:
    n = []

n.extend(l)
save_to_json_file(n, 'add_item.json')
