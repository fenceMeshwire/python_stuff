#!/usr/bin/env python3

# Python 3.9.5

# translate_ascii_ord_chr.py

def get_symbol(number):
    return chr(number)

def get_symbol_number(symbol):
    return ord(symbol)

if __name__ == '__main__':
    # Returns the symbol to the corresponding ASCII number: 36 -> '$'
    symbol = get_symbol(36)
    print(symbol)
    # Returns the number to the corresponding ASCII symbol: '$' -> 36
    symbol_number = get_symbol_number('$')
    print(symbol_number)
