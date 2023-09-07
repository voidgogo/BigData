import numpy as np
import random

n = int(input("input number : "))
l = [random.randint(1, 100) for i in range(n)]
v = np.array(l, dtype='int16')
print(v)
# print(v.ndim, v.shape, v.data, v.dtype, v.strides)
