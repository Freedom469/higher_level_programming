#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Defined a square"""
    def __init__(self, size=0):
        """Instantiation of the sqaure class
        Args: size - size of the square
        Raises:
        TypeError: if size is not type int
        ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of a square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Defined object area
        Returns: area of the class square
        """

        return (self.__size ** 2)
