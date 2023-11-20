#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    t = 0
    m = 0
    while m < x:
        try:
            print("{:d}".format(my_list[m]), end='')
            t += 1
        except (TypeError, ValueError):
            pass
        m += 1
    print()
    return t
