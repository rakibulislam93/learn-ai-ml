
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# access the first element
print(arr[0])

# access 2d array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d[1][0]) # output : 4


# access 3d array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("access from 3d array : ",arr_3d[1][1][2]) # output : 12

# negative indexing
neg_arr = np.array([[1, 2, 3], [4, 5, 6]])
print("negative indexing : ",neg_arr[-1][-2]) # output : 5