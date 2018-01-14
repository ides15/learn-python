"""
    For learning Python lists

    USAGE:
    In a command prompt, navigate to this directory and run `python ./lists.py`
"""

#------------------------------
# Making, accessing, deleting lists
#------------------------------

NUMBERS = [5, -6, 2, 4, -5, 1]
NAMES = ['john', 'luke', 'brian', 'connor']

print(NAMES[0])
# print(NAMES[5])

print(NAMES)
del NAMES[3]
print(NAMES)

STRING = 'hello world'
print(STRING[6])



#------------------------------
# Appending and removing elements
#------------------------------

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f']
print(ALPHABET)

ALPHABET.append('g')
ALPHABET.append('h')
print(ALPHABET)

ALPHABET = ALPHABET + ['i', 'j', 'k']
print(ALPHABET)

D_INDEX = ALPHABET.index('d')
print('d index is ' + str(D_INDEX))
del ALPHABET[D_INDEX]
print(ALPHABET)

ALPHABET.remove('c')
print(ALPHABET)

# ALPHABET.remove('d')



#------------------------------
# List API
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#------------------------------

ALPHA_1 = ['a', 'e', 'd', 'c', 'b']
ALPHA_2 = ['g', 'i', 'h']
ALPHA_3 = 'jklmnopqrstuvwxyz'

print(ALPHA_1)
print(ALPHA_2)
ALPHA_1.sort()
ALPHA_2.sort()
print(ALPHA_1)
print(ALPHA_2)

ALPHA_1.insert(5, 'f')
print(ALPHA_1)

ALPHA_1 = '-'.join(ALPHA_1)
print(ALPHA_1)

ALPHA_2 = '-'.join(ALPHA_2)
print(ALPHA_2)

ALPHA_FULL = ALPHA_1 + ALPHA_2 + ALPHA_3
print(ALPHA_FULL)
