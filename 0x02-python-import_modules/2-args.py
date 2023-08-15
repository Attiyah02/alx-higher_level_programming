#!/usr/bin/python3
# Prints the number of arguements and  its lists
if __name__ == "__main__":
    import sys

    arg = sys.argv
    sizeno = len(arg) - 1

    if sizeno > 1:
        print("{} arguments:".format(sizeno))
        for i in range(1, sizeno + 1):
            print("{}: {}".format(i, arg[i]))

    elif sizeno == 0:
        print("{} arguments.".format(sizeno))

    else:
        print("{} argument:".format(sizeno))
        print("{}: {}".format(sizeno, arg[1]))
