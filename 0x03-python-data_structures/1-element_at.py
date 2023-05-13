#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        raise IndexError("Index must be non-negative")
    if idx >= len(my_list):
        raise IndexError("Index out range")
    return my_list[idx]

