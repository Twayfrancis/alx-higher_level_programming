#!/usr/bin/python3
"""defines function that returns object rep by JSON string"""


def from_json_string(my_str):
    """returns an obj rep by JSON string"""
    import json
    return json.loads(my_str)
