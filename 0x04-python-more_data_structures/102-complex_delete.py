#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_d = a_dictionary.copy()
    for key, search in a_dictionary.items():
        if search == value:
            del copy_d[key]
    return copy_d
