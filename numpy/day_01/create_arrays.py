
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(type(arr))

# 0 dimensional array
arr_0d = np.array(40)
print(arr_0d)

# 1 dimensional array
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)

# 2 dimensional array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# 3 dimensional array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d)

# check dimensions
print(arr_0d.ndim)
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

# higher dimensional array
h_arr = np.array([1, 2, 3], ndmin=2)
print(h_arr)
print(h_arr.ndim)