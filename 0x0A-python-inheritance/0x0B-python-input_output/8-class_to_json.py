#!/usr/bin/python3
"""Module that defines a Python class-to-JSON function"""


def class_to_json(obj):
    """The function returns the dictionary representation of a simple data structure"""
    return obj.__dict__
