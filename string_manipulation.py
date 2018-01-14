"""
    For learning Python string manipulation

    USAGE:
    In a command prompt, navigate to this directory and run `python ./string_manipulation.py`
"""

#------------------------------
# Different types of strings
#------------------------------

SINGLE_QUOTE_STRING = 'I am a single quote string'
DOUBLE_QUOTE_STRING = "I am a double quote string"

SENTENCE_ONE = 'I "really" like chocolate'
SENTENCE_TWO = "I 'really' like chocolate"
SENTENCE_THREE = 'I \'really\' like chocolate'

print(SENTENCE_ONE)
print(SENTENCE_TWO)
print(SENTENCE_THREE)

PARAGRAPH = """
This is
a
long paragraph
"""

"""
    Triple quote strings can also be used as comments
    and can span multiple lines
"""

print(PARAGRAPH)

#------------------------------
# Comments
#------------------------------

# This is a single line comment

"""
    This is
    a
    multiple
    line comment
"""

#------------------------------
# String API
# https://docs.python.org/3/library/stdtypes.html#string-methods
#------------------------------

SCIENCE = 'SCIENCE'
print(SCIENCE)
APPLE = 'apples'
print(APPLE)

APPLE = APPLE.upper()
print(APPLE)

SCIENCE = SCIENCE.lower()
print(SCIENCE)

SCIENCE = SCIENCE.title()
print(SCIENCE)

APPLE = '          apple         '
print(APPLE)
APPLE = APPLE.strip().upper()
print(APPLE)



#------------------------------
# String concatenation, .replace, .count
#------------------------------

PREFIX = 'python is an '
SUFFIX = 'awesome language'

FULL = PREFIX + SUFFIX
print(FULL)

FULL = FULL.replace('language', 'snake')
print(FULL)

FULL = FULL * 2
FULL = FULL.replace('snake', 'language, ')
print(FULL)

FULL = FULL.replace('language', 'snake', 1)
print(FULL)

print(FULL.count("an"))



#------------------------------
# String formatting
#------------------------------

N = 11
F = 1.2345678
S = 'computer'

print('my number is {:d}'.format(N))
# `d` stands for format as a decimal (base-10)

print('my number is {:b}'.format(N))
# `b` stands for format as binary

# `e` - exponents
# `b` - binary
# `o` - octal
# `d` - decimal
# `x` - hexidecimal
# `f` - floats
# `s` - strings (default)

print('my number is {:}'.format(N))

print('{:f}'.format(F))

print('{:.3f}'.format(F))
# prints the last 3 digits after the decimal of F and rounds

print('{:011.3f}'.format(F))
# prints formatted F with 11 characters of `0` padding before

print('{0}, {1}, {2}'.format(N, F, S))

print('{name} own(s) {amount} of {object}'.format(
    name='John',
    amount=12,
    object='mangos',
))
