#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        biggest = None
        keyval = 0
        for key, val in a_dictionary.items():
            if val > keyval:
                biggest = key
                keyval = val
        return biggest
    
