#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    my_max = my_list[0]
    for x in my_list[1:]:
        if x > my_max:
            my_max = x
    return my_max
