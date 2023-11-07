#!/usr/bin/python3
'''writes a string'''


def append_write(filename="", text=""):
    '''writes a string'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
