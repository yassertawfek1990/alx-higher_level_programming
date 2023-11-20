#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t = 0
    try:
        while m is not x:
            print(my_list[m], end = "")
            t += 1
    except IndexError:
        None
    print("")
    return (t)
