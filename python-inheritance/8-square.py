#!/usr/bin/python3
"""
    docstring documentation
    A square class that inherits from the 7-rectangle with
    instantiation that initializes the size, which must be
    private and a positive integer. The area method must be
    implemented.
"""


BaseGeometry = __import__('7-rectangle').BaseGeometry


class Square(BaseGeometry):
    """ The square class inheriting from rectangle class. """

    def __init__(self, size):
        """ The method initializes the size to be a positive int
            and set to be a private variable. """
        super().integer_validator("size", size)
        self._size = size

    def area(self):
        """ Calculates and returns the area of the square. """
        return self._size * self._size

    def __str__(self):
        """ Returns the size of the square and name rectangle. """
        width = str(self._size)
        return "[Rectangle] " + width + "/" + width 
