#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end = "")
        except IndexError:
            break
        t += 1
    print("")
    return (t)
