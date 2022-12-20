#!/usr/bin/python3


class Square:
    """creats a square """

    def __init__(self, size=0):
        """initializes a square
	Args:
            size: size of the square
	Raises:
        TypeError: if size is not an integer
	ValueError: if size is less than zero
	"""
        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

