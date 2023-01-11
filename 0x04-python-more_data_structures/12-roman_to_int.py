#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    values = {"I": 1, "V": 5, "X": 10, "L": 50,
               "C": 100, "D": 500, "M": 1000}
    sum = 0
    length = len(roman_string)
    for i in range(0, length):
        first = roman_string[i]
        second = roman_string[i]
        if (i + 1) < len(roman_string):
            second = roman_string[i + 1]
        if values[first] < values[second]:
            sum += -values[first]
        else:
            sum += values[first]
    return sum
