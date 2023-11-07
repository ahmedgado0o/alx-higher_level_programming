#!/usr/bin/python3
'''writes object with json'''


import json


def save_to_json_file(my_obj, filename):
    '''write object with json'''
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
