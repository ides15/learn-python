# pronounced 'decks'

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