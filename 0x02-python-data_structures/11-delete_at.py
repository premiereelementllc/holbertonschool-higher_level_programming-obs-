#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    if idx < 0 or len(my_list) <= idx:
        return my_list

    try:
        del my_list[idx]
    except:
        pass

    return my_list 
