"""
    For exporting into modules.py for learning about modules

    USAGE:
    In a command prompt, navigate to this directory and run `python ./modules.py`
    (./modules.py imports ./volumes.py and uses it's functions)
"""

from math import pi

def sphere_vol(radius):
    """ calculates and returns the volume of a sphere """
    return 4/3 * pi * radius**3

def cube_vol(length, width, height):
    """ calculates and returns the volume of a cube """
    return length * width * height

def cone_vol(radius, height):
    """ calculates and returns the volume of a cone """
    return (pi * radius**2) * height / 3

print('From volumes.py: ', __name__)

def first_half(word):
    """ returns the first half of the given word """
    return word[:int(len(word)/2)]

def last_half(word):
    """ returns the last half of the given word """
    return word[int(len(word)/2):]

if __name__ == '__main__':
    print('Testing string halving functions...')
    assert first_half('abcd') == 'ab', 'first_half failed'
    assert last_half('abcd') == 'cd', 'last_half failed'
    print('All tests passed.')
