#!/usr/bin/python3
""" A rectangle class that inherits from BaseGeometry - 5-base_geometry class
    has the instantiation of the width and height. The width and height
    must be private with no getter or setter and be positive.
"""

BaseGeometry = _import_('6-rectangle.py').BaseGeometry


class Rectangle(BaseGeometry):
    """ Basing the class on the BaseGeometry class, ractangle inherits """

    def _init_(self, width, height):
        # Call the integer validator method from the 6-base_geometry class.
        # Use the super method to call the super class
        super().integer_validation("height", height)
        super().integer_validation("width", width)

        # The initialization of the width and height which must be private with
        # no getter or setter and be positive
        self._width = width
        self._height = height
