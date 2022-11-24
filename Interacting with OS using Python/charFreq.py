#!/usr/bin/env python3

def character_frequency(filename):
    '''Counts the frequency of each character in the given file.'''
    #first try to open file
    try:
        file = open(filename)
    except OSError:
        return None

    #now process file
    characters = {}
    for line in file:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters
