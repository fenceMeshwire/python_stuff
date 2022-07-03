#!/usr/bin/env python3

# Python 3.9.5

# translate_utf_ord_chr.py

def get_symbol(number):
    return chr(number)

def get_symbol_number(symbol):
    return ord(symbol)

if __name__ == '__main__':
    # ascii = [i for i in range(33, 128, 1)]
    # Returns the symbol to the corresponding unicode number: 36 -> '$'
    symbol = get_symbol(36)
    print(symbol)
    # Returns the number to the corresponding unicode symbol: '$' -> 36
    symbol_number = get_symbol_number('$')
    print(symbol_number)
