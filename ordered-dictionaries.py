from collections import OrderedDict

od1 = OrderedDict()
od1['one'] = 1
od1['two'] = 2
od1['three'] = 3
od1['four'] = 4
od1['five'] = 5
od1['six'] = 6

od2 = OrderedDict()
od1['two'] = 2
od1['one'] = 1

print(od1 == od2)

od3 = OrderedDict()
od3['one'] = 1
od3['two'] = 2

print(od1 == od3)
# only equal if they are same keys and values AND same insertion order

od4 = od1
print(od4)
od4 = OrderedDict(sorted(od1.items(), key=lambda t: (4*t[1]) - t[1]**2))
# 3, 4, 3, 0, -5, -12
print(od4)