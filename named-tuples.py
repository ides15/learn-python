from collections import namedtuple

space = namedtuple('space', 'x y z')
print(space)

s1 = space(x=2.0, y=4.0, z=10)
print(s1)

print(s1.x * s1.y * s1.z)


space2 = namedtuple('space2', 'x def z', rename=True)
s1 = space2(3, 4, 5)

# print(s1.def)

print(s1._1)
print(s1.x)
print(s1.z)

sl = [7, 8, 9]
print(space._make(sl))
slTuple = space._make(sl)

print(slTuple.x)

print(slTuple._asdict())

print(slTuple._replace(x=6, z=8))