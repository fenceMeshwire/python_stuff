#!/usr/bin/env python3

# calcSumString.py

# Purpose: Build the decimal checksum from characters [a-zA-Z] of a given string.

import re

class CheckString():

    def __init__(self, string):
        self.strValue = string

    def calcSumValue(self):

        dictLetters = {
        'a': 1, 'b': 2,'c': 3,'d': 4,'e': 5, 'f': 6,'g': 7,'h': 8,
        'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,
        'q': 17,'r': 18, 's': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,
        'y': 25,'z': 26
        }

        self.strValue = self.strValue.lower()
        value:int = 0
        if self.checkString() == True:
            for char in self.strValue:
                strChar = char
                intChar = dictLetters[strChar]
                print(str("'" + strChar + "'"), intChar)
                value += intChar
            print('The checksum for "{}" equals: {} decimal'.format(self.strValue, value))
        else:
            print('Please check the structure of your input string.\nIt has to follow the regEx rule [a-zA-Z].')

    def checkString(self):
        bleString = False
        regExp = '[a-zA-Z]'
        for letter in self.strValue:
            if re.match(regExp ,letter) != None:
                bleString = True
            else:
                bleString = False
        return bleString

string = 'Test'

chkSum = CheckString(string)
chkSum.calcSumValue()
