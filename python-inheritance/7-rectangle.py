#!/usr/bin/python3
"""
    docstring documentation
    A reactangle class with the base geometry with height and width
    initialized and positive integers.The class also returns the
    area and properties of the rectangle, ie width, hieght etc.
"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Ractangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self._width = width
        self._height = height

    def area(self):
        """ Method calculating and returning the rectangle's area. """
        return self._width * self._height

    def string(self):
        """ Method that returns and prints the description of the
        # rectangle. """
        width = str(self._width)
        length = str(self._length)
        return "[" + __class__.__name__ + "]" + width + "/" + length
