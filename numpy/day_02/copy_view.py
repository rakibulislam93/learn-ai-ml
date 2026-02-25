import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = np.copy(arr)
print(arr)
print(x)

arr[0] = 10
print(arr) # output : [10  2  3  4  5]
print(x) # output : [1 2 3 4 5]


# view
y = arr.view()
print(arr)
print(y)

arr[0] = 20
print(arr) # output : [20  2  3  4  5]
print(y) # output : [20  2  3  4  5]

"""
Copy vs View
1. Copy just creates new array
"""