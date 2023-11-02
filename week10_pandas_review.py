import numpy as np
a1 = np.arange(1, 6)
a2 = np.array([6, 7, 8, 9, 10])
a3 = np.array([
    [3, 2, 1],
    [-11, 0, 9]
])
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
print(np.dot(a1, a2))
# a3 = a1 + a2
# print(a3)
print(np.sum(a1) + np.sum(a2))
print(np.prod(a1), np.prod(a2))
# by axis
print(a3.sum(axis=0))
print(a3.sum(axis=1))
print(a3.prod(axis=0))
print(a3.prod(axis=1))
print(a3.mean())  # 산술평균
print(a3.std())  # 표준편차