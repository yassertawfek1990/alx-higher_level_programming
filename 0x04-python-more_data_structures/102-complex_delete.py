#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    n = []
    for x in a_dictionary.keys():
        if len(a_dictionary[x]) > 0:
            for j in a_dictionary[x]:
                if j == value:
                    n.append(x)
        else:
            if a_dictionary[x] == value:
                n.append(x)
    for k in n:
        del a_dictionary[k]
    return a_dictionary
