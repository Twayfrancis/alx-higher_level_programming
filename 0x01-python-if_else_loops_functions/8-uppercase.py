#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        result += c
    print(result)
