#!/usr/bin/python3
'''creats object from json'''


import json


def load_from_json_file(filename):
    '''creats object'''
    with open(filename, 'r', encoding="utf-8") as f:
        return json.lead(f)
