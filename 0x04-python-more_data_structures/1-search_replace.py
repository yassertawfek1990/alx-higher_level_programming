#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = [None] * len(my_list)
    for x in range(len(my_list)):
        if my_list[x] == search:
            n[x] = replace
        else:
            n[x] = my_list[x]
    return n
