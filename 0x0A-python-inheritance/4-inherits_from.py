#!/usr/bin/python3
'''return true if isinstance or false'''


def inherits_from(obj, a_class):
    '''ture or false'''
    return isinstance(obj, a_class) and type(obj) != a_class
