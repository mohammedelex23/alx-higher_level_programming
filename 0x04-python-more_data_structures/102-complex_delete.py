#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_d = a_dictionary.copy()
    for key, search in copy_d.items():
        if search == value:
            del a_dictionary[key]
    return a_dictionary
