#!/usr/bin/pyton3
def safe_print_division(a, b):
    n_integers = 0
    try:
        n_integers = a/ b
    except (ZeroDivisionError, FloatingPointError):
        n_integers = None
    finally:
        print("Inside result:{}".format(n_integers))
    return n_integers
