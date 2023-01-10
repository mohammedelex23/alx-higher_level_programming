#!/usr/bin/python3
def new_in_list(my_list, idx, element):
<<<<<<< HEAD
    new_list = my_list.copy()
        if idx in range(0, len(my_list)):
           _list[idx] = element
    return new_list
=======
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    temp_list = list(my_list)
    temp_list[idx] = element
    return temp_list
>>>>>>> 176a20ab6de44d5d0202cf38ab921650e4e913c1
