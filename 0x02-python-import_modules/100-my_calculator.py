#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    ops = "+-*/"
    argvlen = len(sys.argv)
    if argvlen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    args = sys.argv
    a = int(args[1])
    operator = args[2]
    b = int(args[3])
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if (operator == "+"):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (operator == "-"):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (operator == "*"):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
