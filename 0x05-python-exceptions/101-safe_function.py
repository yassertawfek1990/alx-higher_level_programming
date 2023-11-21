#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        r = fct(*args)
        return (r)
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return (None)
