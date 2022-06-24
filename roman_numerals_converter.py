#!/usr/bin/env python3

# Python 3.9.5

# roman_numerals_converter.py

def convert_roman(decimal_number):
    
    roman_number:str = ''
    roman_numbers_millions = {3000000:u'M\u0305M\u0305M\u0305', 2000000:u'M\u0305M\u0305', 1000000:u'M\u0305'}
    roman_numbers_hundred_thousands = {900000:u'C\u0305M\u0305', 800000:u'D\u0305C\u0305C\u0305C\u0305', 
                                    700000:u'D\u0305C\u0305C\u0305', 600000:u'D\u0305C\u0305',500000:u'D\u0305', 
                                    400000:u'C\u0305D\u0305', 30000:u'D\u0305D\u0305D\u0305', 200000:u'D\u0305D\u0305', 
                                    100000:u'D\u0305'}
    roman_numbers_ten_thousands = {90000:u'X\u0305C\u0305', 80000:u'L\u0305X\u0305X\u0305X\u0305', 
                                    70000:u'L\u0305X\u0305X\u0305', 60000:u'L\u0305X\u0305',50000:u'L\u0305', 
                                    40000:u'X\u0305L\u0305', 30000:u'X\u0305X\u0305X\u0305', 20000:u'X\u0305X\u0305', 
                                    10000:u'X\u0305'}
    roman_numbers_thousand = {9000:u'I\u0305X\u0305', 8000:u'V\u0305MMM', 7000:u'V\u0305MM', 6000:u'V\u0305M', 
                                5000:u'V\u0305', 4000:u'I\u0305V\u0305', 3000:'MMM', 2000:'MM', 1000:'M'}
    roman_numbers_hundreds = {900:'CM', 800:'DCCC', 700:'DCC', 600:'DC', 500:'D', 400:'CD', 300:'CCC', 200:'CC', 100:'C'}
    roman_numbers_tens = {90:'XC', 80:'LXXX', 70:'LXX', 60:'LX', 50:'L', 40:'XL', 30:'XXX', 20:'XX', 10:'X'}
    roman_numbers_ones = {9:'IX', 8:'VIII', 7:'VII', 6:'VI', 5:'V', 4:'IV', 3:'III', 2:'II', 1:'I'}

    millions = decimal_number // 1000000
    rest = decimal_number - millions * 1000000
    if millions > 0:
        print(1000000*millions,':', roman_numbers_millions[1000000*millions])
        roman_number += roman_numbers_millions[1000000*millions]

    hundred_thousands = rest // 100000
    rest = rest - hundred_thousands * 100000
    if hundred_thousands > 0:
        print(100000*hundred_thousands,'\t:', roman_numbers_hundred_thousands[100000*hundred_thousands])
        roman_number += roman_numbers_hundred_thousands[100000*hundred_thousands]

    ten_thousands = rest // 10000
    rest = rest - ten_thousands * 10000
    if ten_thousands > 0:
        print(10000*ten_thousands,'\t:', roman_numbers_ten_thousands[10000*ten_thousands])
        roman_number += roman_numbers_ten_thousands[10000*ten_thousands]

    thousands = rest // 1000
    rest = rest - thousands * 1000
    if thousands > 0:
        print(1000*thousands,'\t:', roman_numbers_thousand[1000*thousands])
        roman_number += roman_numbers_thousand[1000*thousands]
    
    hundreds = rest // 100
    rest = rest - hundreds * 100
    if hundreds > 0:
        print(100*hundreds,'\t:', roman_numbers_hundreds[hundreds*100])
        roman_number += roman_numbers_hundreds[hundreds*100]

    tens = rest // 10
    rest = rest - tens * 10
    if tens > 0:
        print(10*tens,'\t:', roman_numbers_tens[tens*10])
        roman_number += roman_numbers_tens[tens*10]
    
    ones = rest
    if ones > 0:
        print(ones,'\t:', roman_numbers_ones[ones])
        roman_number += roman_numbers_ones[ones]

    print('Total:')
    print(decimal_number,'\t:', roman_number)

    return roman_number

if __name__ == '__main__':
    decimal_sample = 1234
    if 1 <= decimal_sample <= 3999999:
        roman_number = convert_roman(decimal_sample)
    else:
        print('Roman numbers must be in range of 1 to 3.999.999')
