#!/usr/bin/python3
"""
    function that returns True if the object is an instance of the class,
    or if the object is an instance of a class that is inherited from the
    speficied class, else returns False
"""


def is_kind_of_class(obj, a_class):
    """ the obj is kind of the class """
    return isinstance(obj, a_class)
