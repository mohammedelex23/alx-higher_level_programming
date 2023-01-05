#!/usr/bin/python3
import sys
if __name__ == "__main__":
        arguments = sys.argv
            length = len(arguments)
                if length == 1:
                            print("0 arguments.")
                                    exit
                elif length == 2:
                            print("1 argument:")
                else:
                            print("{} arguments".format(length - 1))
                                for index in range(1,length):
                                            print("{}: {}".format(index, arguments[index]))
                                            
