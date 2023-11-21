#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
        return (r)
    except Exception as x:
        print("Exception: ", x, file=sys.stderr)
        return (None)
