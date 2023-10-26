import numpy as np

np_1d = np.arange(1, 20, 2)
#np_1d = np.arange(1.0, 10.0, 2.0)
np_1d = np_1d.reshape(5, 2)
print(np_1d, type(np_1d))
print(np_1d, type(np_1d[0]))
print(np_1d.ndim)  # n-dimension, rank
print(np_1d.size)  # size
print(np_1d.shape)  # shape


# np_1d = np.array([2, 4, 6, 8])
# np_2d = np.array([[2, 4], [6, 8]])
# print(np_1d.ndim, np_2d.ndim)  # n-dimension, rank
# print(np_1d.size, np_2d.size)  # size
# print(np_1d.shape, np_2d.shape)  # shape


# any_list = [91, "university", 3.91, (5, 7)]
# converted_any_list = ["91", "university", "3.91", "(5, 7)"]
#one_type_np_list = np.array(converted_any_list)
#one_type_np_list = np.array(any_list)  # ValueError

# for i in any_list:
#     print(i)
#
# for j in one_type_np_list:
#     print(j)
