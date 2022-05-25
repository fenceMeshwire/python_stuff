#!/usr/bin/env python3

# Python 3.9.7

# directory_from_spreadsheet.py

# Dependencies
import os, re

def get_special_spreadsheets(directory, spreadsheets):
    file_regex = re.compile(r'\D\D\d\d') # Pattern like AB12
    for file in os.listdir(directory):
        if 'xls' in file:
            spreadsheet = file.split('.')
            spreadsheet = spreadsheet[0]
            result = file_regex.match(spreadsheet)
            if result != None:
                spreadsheets.append(spreadsheet)
    return spreadsheets

def create_directories(directory, spreadsheets):
    intCounter = 0
    for spreadsheet in spreadsheets:
        intCounter += 1
        if intCounter < 10:
            directory_name = '0' + str(intCounter) + '_' + spreadsheet
        else: 
            directory_name = str(intCounter) + '_' + spreadsheet
        target_directory = os.path.join(directory, directory_name)
        if os.path.exists(target_directory):
            pass
        else:
            os.makedirs(target_directory)

if __name__ == '__main__':
    directory = 'C:\\Users\\...'
    spreadsheets = []
    spreadsheets = get_special_spreadsheets(directory, spreadsheets)
    create_directories(directory, spreadsheets)
