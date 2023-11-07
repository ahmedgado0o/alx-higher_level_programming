#!/usr/bin/python3
'''reads a file and print to stan  output'''


def read_file(filename=""):
    '''reads file and print'''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
