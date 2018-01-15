"""
    For learning Python conditionals

    USAGE:
    In a command prompt, navigate to this directory and run `python ./conditionals.py`
"""

#------------------------------
# If statements
#------------

AGE = 35

if AGE == 35:
    print('Age is equal to 35')

NAME = 'Megan'

if NAME == 'Megan':
    print('Yes, my name is Megan')

    if AGE == 35:
        print('Megan\'s age is equal to 35')

print()



#------------------------------
# else and elif statements
#------------

NAME = 'John'

if NAME == 'John':
    print('Name is John')
else:
    print('Name is not John')

if NAME == 'Emily':
    print('Name is Emily')
elif NAME == 'Megan':
    print('Name is Megan')
else:
    print('Name is John')

print()



#------------------------------
# and, or, not
#------------

T = True
F = False

if T or T:
    print('T or T')
if T or F:
    print('T or F')
if F or T:
    print('F or T')
if F or F:
    print('F or F')

print()

if T and T:
    print('T and T')
if T and F:
    print('T and F')
if F and T:
    print('F and T')
if F and F:
    print('F and F')

print()

print(not 3 == 6)
print(not 4 > 2)

print()



#------------------------------
# Examples
#------------

FIRST = int(input())
SECOND = int(input())

if FIRST % SECOND == 0 or SECOND % FIRST == 0:
    print('Divisible')
else:
    print('Not divisible')

print()

A = int(input())
B = int(input())

if B is not 0:
    print(A / B)

print()

NAME_1 = str(input('name 1 = ')).lower()
NAME_2 = str(input('name 2 = ')).lower()
NAME_3 = str(input('name 3 = ')).lower()

if NAME_1 == NAME_2 == NAME_3:
    print('All 3 names are equal')
else:
    print('Names are not equal')

print()

import sys

LINE = input()
SPLIT = LINE.split()

LEFT = int(SPLIT[0])
OP = SPLIT[1]
RIGHT = int(SPLIT[2])

VAL = 0

if OP == '+':
    VAL = LEFT + RIGHT
elif OP == '-':
    VAL = LEFT - RIGHT
elif OP == '*':
    VAL = LEFT * RIGHT
elif OP == '/':
    if RIGHT == 0:
        print('Undefined')
        sys.exit()
    VAL = LEFT / RIGHT
else:
    print('Unknown operator: {operator}'.format(operator=OP))

print(VAL)
