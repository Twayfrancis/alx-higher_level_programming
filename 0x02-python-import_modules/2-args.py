#!/usr/bin/python3
import sys
if __name__ == '__main__':
    num = len(sys.argv) - 1
    arg_list = sys.argv[1:]
    print("{} argument{}:".format(num, 's' if num != 1 else ''), end='')

    if num == 0:
        print(".")
    else:
        print()
        for i, arg in enumerate(arg_list, start=1):
            print("{}: {}".format(i, arg))
