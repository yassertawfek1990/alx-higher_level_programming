#!/usr/bin/python3
"""define ffsf"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        it = load_from_json_file("add_item.json")
    except Exception:
        it = []
    it.extend(sys.argv[1:])
    save_to_json_file(it, "add_item.json")
