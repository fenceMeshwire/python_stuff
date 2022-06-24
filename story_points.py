#!/usr/bin/env python3

# Python 3.9.5

# storyPoints.py

import numpy as np
import matplotlib.pyplot as plt

story_points = [1, 3, 5, 8, 13]

sp = np.array([1, 3, 5, 8, 13])
mean_sp = np.mean(sp)
mean_sp # Mean 6.0
diff_sp = np.diff(sp)
diff_sp # Difference: 2, 2, 3, 5
std_sp = np.std(sp)
std_sp # Standard Deviaton = 4.195

def prime(n): # Check if a story point is a prime number
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

sp_primes = []
for story_point in story_points:
    sp_primes.append(prime(story_point))
sp_primes # [True, True, True, False, True]

xAxis = [x for x in range(1, len(story_points)+1)]
plt.xkcd()
plt.plot(xAxis, story_points, marker='o')
plt.ylabel('Story Points')
plt.show()
