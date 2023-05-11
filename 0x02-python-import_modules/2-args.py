#!/usr/bin/python3
import sys
if __name__== '__main__':
    num_args = len(sys.argv) - 1
    arg_list = sys.argv[1:]
    print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''), end='')
    if num_args == 0:
        print(".")
    else:
        print()
        for i, arg in enumerate(arg_list, start=1):
            print("{}: {}".format(i, arg))
