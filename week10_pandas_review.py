import numpy as np
from numpy.linalg import inv
# linalg == linear algebra
np.random.seed()
X = np.array([
    [1, 2, 3],
    [1, 0, 0],
    [0, 0, 1]
])
print(X)
Z = inv(X)  # 역행렬
print(Z)
print(X.dot(Z))
