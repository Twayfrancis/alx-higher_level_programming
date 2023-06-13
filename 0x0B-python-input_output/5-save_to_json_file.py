#!/usr/bin/python3
"""deffines function that writes obj to a txt file, using json rep"""


def save_to_json_file(my_obj, filename):
    """writes an object to txt file, using json rep, return none"""
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
