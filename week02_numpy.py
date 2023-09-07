import numpy as np

# v = np.array([1, 3, -9, 2])
# v = np.array([1, 3, -9, 2], dtype='int64')
v = np.array([
    [1, 3, -9, 2],
    [71, 13, -22, 7]])#, dtype='int64')
print(v.ndim, v.shape, v.data, v.dtype, v.strides)
