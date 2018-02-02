a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
t = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

print(type(a))
print(len(a))
print(a.difference(t))
print(a.intersection(t))
print(a.isdisjoint(t))
print(a.issubset(t))
print(a.issuperset(t))
print(a.symmetric_difference(t))
print(a.union(t))

a.add(10)
print(a)

a.clear()
print(a)

a.pop()
print(a)

