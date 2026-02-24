import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# slicing 1d array
print(arr[0:5:2])# output : [1 3 5]

# slicing 2d array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d[1, :2]) # output : [4 5]

print(arr_2d[:2,:2]) # output : [[1 2][4 5]]