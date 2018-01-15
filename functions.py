"""
    For learning Python functions

    USAGE:
    In a command prompt, navigate to this directory and run `python ./functions.py`
"""

#------------------------------
# Using functions
#------------

PI = 3.14159

def circle_area(radius):
    """ Finds the area of a circle with the radius of param `r` """
    return PI * radius**2

USER_RADIUS = int(input())

print(circle_area(USER_RADIUS))



#------------------------------
# Infinite parameters
#------------

def add(*numbers):
    """ Adds up however many numbers are given as arguments """
    total = 0
    for number in numbers:
        total += number
    return total

print(add(1, 2, 3, 4, 5, 6))



#------------------------------
# Default parameters
#------------

import datetime as dt

def record_time(message, time=dt.datetime.now()):
    """ Prints the current time to the console """
    print('{:}, time: {:}'.format(
        message,
        time
    ))

record_time('Today')



#------------------------------
# Recursion
#------------

def count_vowels(string, i=0):
    """ recursively counts the number of vowels in a string """
    if i == len(string):
        return 0

    character = string[i]

    if character in 'aeiou':
        return count_vowels(string, i + 1) + 1
    return count_vowels(string, i + 1)
