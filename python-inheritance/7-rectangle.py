#!/usr/bin/python3
"""
    A reactangle class with the base geometry with height and width
    initialized and positive integers.
"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Ractangle(BaseGeometry):
    """ Class inherits from the base geometry class, has width and 
        height initialized and area must be used. """

    def _init_(self, width, height):
        """ Call the integer validator method from 5-base_geometry
            use the super method to call methods from the super 
            class """

        super().integer_validator("height", height)
        super().integer_validator("width", width)
        # Call and initialize the width method.
        self._width = width
        self._height = height

    """ Method that calculates and returns the rectangle's area """
    def area(self):
        return self._width * self._height

    """ Method that returns and prints the area and description of the
        rectangle. """
    def string(self):
        width = str(self._width)
        length = str(self._length)
        return "[" + __class__.__name__ + "]" + width + "/" + length
