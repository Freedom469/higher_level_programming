#!/usr/bin/python3

def sloweist_digit(number):
    digit = abs(number) % 10
    print("{:d}".format(digit), end="")

    return digit
