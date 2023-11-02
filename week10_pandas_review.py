import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.array([
    [5, 20],
    [11, -1],
    [9, 3]
])
print(a)
print(b)
print()
print(a.dot(b))
print(np.dot(a, b))
print(b.dot(a))
print(np.dot(b, a))