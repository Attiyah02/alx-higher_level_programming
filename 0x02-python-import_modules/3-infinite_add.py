#!/usr/bin/python3
def add_arg(argv):
    l = len(argv) - 1
    if l == 0:
        print("{:d}".format(l))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
