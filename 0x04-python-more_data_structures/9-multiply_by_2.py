#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_d = a_dictionary.copy()
    for key in a_dictionary:
        copy_d[key] = copy_d[key] * 2
    return copy_d
