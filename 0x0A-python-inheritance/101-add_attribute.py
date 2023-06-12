#!/usr/bin/python3
"""Adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """ adds a new attribute"""
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
        return
    raise TypeError("can't add new attribute")
