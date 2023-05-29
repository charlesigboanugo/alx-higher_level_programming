#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        return {x: y * 2 for x, y in a_dictionary.copy().items()}
    
