#!/usr/bin/python3
def number_keys(a_dictionary):
    nums = 0
    list_of_keys = list(a_dictionary.keys())

    for i in list_of_keys:
        nums += 1

    return (nums)
