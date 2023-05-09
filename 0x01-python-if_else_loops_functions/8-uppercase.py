#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - ord('a') + ord('A'))), end="")
        else:
            print("{}".format(c), end="")
    print()
