#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t = 0
    for i in range(x):
        try:
            print(my_list[i], end = "")
            t += 1
        except IndexError:
            None
    print()
    return (t)
