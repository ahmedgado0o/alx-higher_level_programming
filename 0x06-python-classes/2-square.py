#!/usr/bin/python3
"""Square class"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: size

        Raises:
            TypeError: error type
            ValueError: value error
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        seld.__size = size
