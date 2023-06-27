#!/usr/bin/python3
"""
    A square class that inherits from the 7-rectangle with
    instantiation that initializes the size, which must be
    private and a positive integer. The area method must be
    implemented.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square:
    """ The square class inheriting from rectangle class. """

    def __init__(self, size):
        """ The method initializes the size, ensure its a
            positive integer and private. """
        super().Integer_validator("size", size)
        self._size = size

    def area(self):
        """ The method calculates the area of the square and
            returns it. """
        return self._size * self._size
