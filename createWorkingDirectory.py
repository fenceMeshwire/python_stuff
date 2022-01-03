#!/usr/bin/env python3

# createWorkingDirectory.py

# Purpose: Create a working directory for a python script.

# Dependencies
import os, platform
from pathlib import Path

class CurrentWorkDirectory(): # Set working directory

    def __init__(self):
        self.posix = '/Users/username'
        self.windows = 'C:\\temp\\username'

    def setWorkingDirectory(self):
        if os.name == 'posix' or platform.system() == 'Darwin': # Check operating system for posix.
            try:
                if os.path.exists(self.posix):
                    print("Directory already exists.")
                    os.chdir(self.posix)
                else:
                    os.makedirs(self.posix)
                    print("Directory created:", self.posix)
                    os.chdir(self.posix)
            except BaseException as err:
                print(err)
        elif os.name == 'nt' or platform.system() == 'Windows': # Check operating system for Windows.
            try:
                if os.path.exists(self.windows):
                    print("Directory already exists.")
                    os.chdir(self.windows)
                else:
                    os.makedirs(self.windows)
                    print("Directory created:", self.windows)
                    os.chdir(self.windows)
            except BaseException as err:
                print(err)
        return Path.cwd() # Check working directory.

oCurrentWorkDirectory = CurrentWorkDirectory()
oCurrentWorkDirectory.setWorkingDirectory()
