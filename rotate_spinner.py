#!/usr/bin/env python3

# Python 3.9.5

# rotate_spinner.py

# Purpose: Create a moving spinner with the characters = ['|', '/', '-', '\\'] 

import random, time

class Rotate():
    def __init__(self, downloadSize):
        self.downloadedBytes = 0
        self.downloadSize = downloadSize
        self.characters = ['|', '/', '-', '\\']

    def spinner(self):
        while self.downloadedBytes < self.downloadSize:
            # Simulation of the download:
            self.downloadedBytes += random.randint(0,1000)

            for char in self.characters:
                print('\b\b', char, end='', flush=True)
                time.sleep(0.05)

        print('\nDownload completed!')
        
downloadSize = 8192

oRotate = Rotate(downloadSize)
oRotate.spinner()
