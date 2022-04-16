#!/usr/bin/env python3

# Python 3.9.5

# 07_findSubstring.py

# Purpose: 
#   1. Find a given substring within a given string.
#   2. Return the position of the first character of the substring within the string.

def findSubstring_iterative(substring, string):
    i = 0
    while i < len(string):
        if string[i:i + len(substring)] == substring:
            return i # Needle found
        i = i + 1
    return -1 # Needle not found

def findSubstring_recursive(substring, string, i=0):
    if i >= len(string):
        return -1 # Base case, substring not found
    if string[i:i + len(substring)] == substring:
        return i # Base case, substring found
    else:
        # Recursive case
        return findSubstring_recursive(substring, string, i + 1)

if __name__ == '__main__':
    findSubstring_iterative('word', 'This sentence contains a word.')
    findSubstring_recursive('word', 'This sentence contains a word.')
