import sys
from array import array

ba = array('i', range(10))

bl = list(range(10**6))

print(sys.getsizeof(ba))
print(sys.getsizeof(bl))
print('The list is', sys.getsizeof(bl) / sys.getsizeof(ba), 'times larger than the array\n')

print(ba)

for count, num in enumerate(ba):
    ba[count] += 1

print(ba)