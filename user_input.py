"""
    For learning Python user input

    USAGE:
    In a command prompt, navigate to this directory and run `python ./user_input.py`
"""

#------------------------------
# Formatting user input
#------------------------------

# firstname, M. lastname

FIRST_NAME = str(input('Please enter your first name: '))
MIDDLE_NAME = str(input('Please enter your middle name: '))
LAST_NAME = str(input('Please enter your last name: '))

FIRST_NAME = FIRST_NAME.capitalize()
MIDDLE_NAME = MIDDLE_NAME.capitalize()
LAST_NAME = LAST_NAME.capitalize()

NAME_FORMAT = '{first} {middle:.1s}. {last}'

print(NAME_FORMAT.format(
    first=FIRST_NAME,
    middle=MIDDLE_NAME,
    last=LAST_NAME,
))
