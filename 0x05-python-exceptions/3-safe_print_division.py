#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        n_integers = a / b
    except (TypeError, ZeroDivisionError):
        n_integers = None
    finally:
        print("Inside result: {}".format(n_integers))
    return n_integers
