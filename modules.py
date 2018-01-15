"""
    For learning Python modules

    USAGE:
    In a command prompt, navigate to this directory and run `python ./modules.py`
"""
import math
from math import pi
from math import factorial as f
from PIL import Image

import volumes
from volumes import sphere_vol

#------------------------------
# `import`, `as`, and `from` statements
#------------


print(math.pi)
print(math.cos(math.pi))

print(pi)


print(f(3))



#------------------------------
# Creating modules
#------------


print(dir(volumes))

print(volumes.cube_vol(2, 3, 4))

print(sphere_vol(4))

print()



#------------------------------
# Creating modules
#------------

print('From modules.py: ', __name__)



#------------------------------
# Using 3rd party library with pip
#------------

JOHN_MOM_IMG = Image.open('john-mom-900.jpg')

JOHN_MOM_IMG.show()
