#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argvlen = len(sys.argv)
    if argvlen == 1:
        print(0)
    else:
        args = sys.argv
        sum = 0
        for index in range(1, len(args)):
            arg = int(args[index])
            sum += arg
        print(sum)
