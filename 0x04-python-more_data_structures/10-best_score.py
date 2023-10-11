#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for x, y in a_dictionary.items():
        if y > maxval:
            maxval = y
            maxkey = x
    return maxkey
