#!/usr/bin/python3

def print_sorted_dictionary(my_dict):
    for a in sorted(my_dict.keys()):
        print("{}: {}".format(a, my_dict[a]))
