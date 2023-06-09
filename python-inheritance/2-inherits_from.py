#!/usr/bin/python3
"""
    function that returns True if obj is an instance of a class that inherited 
    either directly or indirectly from the specified class otherwise False.
"""


def inherits_from(obj, a_class):
    """ returns true if the class is a subclass the """ 
    return issubclass(obj, a_class)
