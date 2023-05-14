#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at specified index in the list.
    Args:
    my_list: The list to be processed.
    idx: The index of the item to be deleted.
    Returns: the list with item at specified index deleted.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    my_list.pop()
    return my_list
