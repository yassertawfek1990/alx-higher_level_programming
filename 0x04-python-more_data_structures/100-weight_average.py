#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    t = 1
    c = 0
    w = 0
    for x in range(len(my_list)):
        t = 1
        for i in range(len(my_list[x])):
            t *= my_list[x][i]
        w += my_list[x][1]
        c += t
    return (c / w)
