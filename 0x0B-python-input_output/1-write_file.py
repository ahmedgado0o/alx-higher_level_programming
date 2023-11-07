#!/usr/bin/python3
'''writes a string'''


def write_file(filename="", text=""):
    '''writes a string'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
