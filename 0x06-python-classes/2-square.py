#!/usr/bin/python3
"""Square class"""


def __init__(self, size):
    """Constructor.

    Args:
        size: size
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    seld.__size = size
