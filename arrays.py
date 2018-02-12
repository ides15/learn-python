import sys
from array import array

ba = array('i', range(10))

bl = list(range(10))

print(sys.getsizeof(ba))
print(sys.getsizeof(bl))
print('The list is', sys.getsizeof(bl) / sys.getsizeof(ba), 'times larger than the array\n')

print(ba)

for count, num in enumerate(ba):
    ba[count] += 1

print(ba)

# generators

def creategenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i

mygenerator = creategenerator()
for i in mygenerator:
    print(i)