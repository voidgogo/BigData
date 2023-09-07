import numpy as np
import random

n = int(input("input number : "))
l = list()
for i in range(n):
    l.append(random.randint(1, 100))

v = np.array(l, dtype='int16')
print(v)
print(v.ndim, v.shape, v.data, v.dtype, v.strides)
