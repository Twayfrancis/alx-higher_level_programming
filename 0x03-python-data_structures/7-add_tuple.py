#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        raise ValueError("tuple_a cannot be empty")
    try:
        first_element = tuple_a[0] + tuple_b[0]
        second_element = tuple_a[1] if len(tuple_a) > 1 else 0
    except IndexError:
        second_element = 0

    return (first_element, second_element)
