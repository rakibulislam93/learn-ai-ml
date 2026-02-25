import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype) # output : int64

arr_float = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(arr_float.dtype) # output : float64

arr_srt = np.array(["apple", "bananas", "cherry"])
print(arr_srt.dtype) # output : <U6

arr1 = np.array([1,2,3,4], dtype='S')
print(arr1) # output : [b'1' b'2' b'3' b'4']
print(arr1.dtype) # output : |S1

arr2 = np.array([1,2,3,4], dtype='U')
print(arr2) # output : ['1' '2' '3' '4']
print(arr2.dtype) # output : <U1

arr3 = np.array([1,2,3,4], dtype='i8')
print(arr3) # output : [1 2 3 4]
print(arr3.dtype) 



arr4 = np.array([1.2,2.3,4.5])
new_arr4 = arr4.astype('i')
print(new_arr4) # output : [1 2 4]
print(new_arr4.dtype) # output : int32


"""
i = interger
f = float
S = string
b = boolean
c = complex
m = timedelta
M = datetime
O = object
U = unicode string
V = void
u = unsigned interger
"""