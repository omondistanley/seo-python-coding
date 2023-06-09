#!/usr/bin/python3
"""
   class based on the base geometry class with a public instance
   method that raises an exception.
"""


class BaseGeometry:
    """ Basing the class on the empty BaseGeometry """

    def area(self):
        """ Public instance method of the area, raises excpetion
        if area isn't use. """
        raise Exception("area() is not implemented")
