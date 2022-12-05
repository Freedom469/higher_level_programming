#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    re = my_list[::-1]
    for i in range(len(re)):
        print("{:d}".format(re[i]))
