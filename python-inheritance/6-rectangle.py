#!/usr/bin/python3
""" A rectangle class that inherits from BaseGeometry - 5-base_geometry class
    has the instantiation of the width and height. The width and height
    must be private with no getter or setter and be positive.
"""


class Rectangle:
    """ Basing the class on the empty BaseGeometry class """

    def area(self):
        """ Public instance methof of the area, raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        # Public instance method that validates the value ensuring its positive
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def _init_(self, width, height):
        # The instantiation of the width and height which must be private with
        # no getter or setter and be positive
        self._width = width
        self._height = height
