#!/usr/bin/python3
"""
    function that returns True if the object is an exact instance of
    the given class and returns False is the object isn't an exact instance
"""


def is_same_class(obj, a_class):
    """ returns true if the object is instance of the class """
    return type(obj) is a_class
