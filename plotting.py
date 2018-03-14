import math
import matplotlib.pyplot as plt

x = list(range(1, 100))

plt.plot(x, [y * y for y in x])
plt.plot(x, [(7 * y) * math.log(y, 2) for y in x])
plt.show()