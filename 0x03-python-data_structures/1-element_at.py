#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    ele = my_list[idx]

    if idx < 0 or idx > length:
        return None
    else:
        return ele
