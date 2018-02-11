from collections import ChainMap
from collections import Counter

defaults = {
    'theme': 'Default',
    'language': 'eng',
    'showIndex': True,
    'showFooter': True
}

cm = ChainMap(defaults)
cm2 = cm.new_child({
    'theme': 'bluesky'
})

# print(cm2['theme'])
# print(cm2.pop('theme'))

# print(cm2['theme'])

cm2.maps[0] = {
    'theme': 'desert',
    'showIndex': False
}

# print(cm2['showIndex'])

# print(cm2.parents)

c1 = Counter('anysequence')
print(c1)

c2 = Counter({
    'a': 1,
    'c': 1,
    'e': 3
})
print(c2)

c3 = Counter(a=1, c=1, e=3)
print(c3)

c3.update(a=4)
print(c3)
# adds 4 occurences of 'a' to c3

# print(c3['b'])
# returns 0, NOT KeyError or falsey

for item in c3:
    print('%c : %d' % (item, c3[item]))

print(c3['a'])
print(c3['b'])

print(c3)
print(sorted(c3.elements()))
print([x for x in c3.elements()])

print(c3)
print(c3.most_common())
print(c3.most_common(2))
print(c3)
c3.subtract({'c': 1})
print(c3)