#!/usr/bin/python3
"""defines function that returns JSON rep of object(string)"""


def to_json_string(my_obj):
    """returns the JSON rep of an object"""
    import json
    return json.dumps(my_obj)
