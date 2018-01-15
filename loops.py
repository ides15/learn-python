"""
    For learning Python loops

    USAGE:
    In a command prompt, navigate to this directory and run `python ./loops.py`
"""

#------------------------------
# `in` keyword
#------------

S = 'hello world'
A = [4, 6, 9]

print(5 in A) # conditional, will eval to false
print(6 in A) # conditional, will eval to true
print(' worl' in S) # conditional, will eval to true

for num in A:
    print(num)

print(range(len(A)))

for index, item in enumerate(A):
    print('Index: {:d}, number: {:d}'.format(
        index,
        item
    ))



#------------------------------
# while loop
#------------

INDEX = 0
NAMES = ['John', 'Brian', 'Connor', 'Luke']

while INDEX < len(NAMES):
    print(NAMES[INDEX])
    INDEX = INDEX + 1



#------------------------------
# try / catch
#------------

MY_LIST = [1, 2, 3, 4, 5]
MY_TUPLE = (2, 7, 8, 9, 10)
MY_STRING = 'Hello World'

LIST_ITERATOR = iter(MY_LIST)

while True:
    try:
        NEXT_ELEM = next(LIST_ITERATOR)
        print(NEXT_ELEM)
    except StopIteration:
        break
