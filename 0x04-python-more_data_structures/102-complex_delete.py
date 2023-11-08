#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    n = list(a_dictionary.keys())
    for x in n:
        if a_dictionary.get(x) == value:
            del a_dictionary[x]
    return (a_dictionary)
