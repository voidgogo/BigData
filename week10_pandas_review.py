import numpy as np
a1 = np.ones((3, 3))
a1[:, 2] = 2
print(a1)
a2 = np.array([
    [1, 0, 0],
    [2, 0, 0],
    [1, 0, 0],
])
print(a2)
print(np.matmul(a1, a2))  # 행렬 곱
