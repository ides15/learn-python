# pronounced 'decks'

import itertools
from collections import deque

dq = deque('abc')
print(dq)

dq.append('d')
print(dq)

dq.appendleft('z')
print(dq)

dq.extend('efg')
print(dq)

dq.extendleft('yxw')
print(dq)

print(dq.pop())
print(dq.popleft())
print(dq)

dq.rotate(2)
print(dq)

dq.rotate(-2)
print(dq)

print(list(itertools.islice(dq, 3, 9)))

print('circular buffer')
dq2 = deque([], maxlen=3)

for i in range(6):
    dq2.append(i)
    print(dq2)