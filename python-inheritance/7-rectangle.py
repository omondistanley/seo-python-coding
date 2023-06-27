#!/usr/bin/python3
"""
    docstring documentation
    A reactangle class with the base geometry with height and width
    initialized and positive integers.The class also returns the
    area and properties of the rectangle, ie width, hieght etc.
"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Basing the class on the BaseGeometry class, rectangle inherits """

    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def __str__(self):
        width = str(self._width)
        length = str(self._length)
        return "[" + __class__.__name__ + "]" + width + "/" + length
