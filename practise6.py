import numpy as np

#Shape of an array is the number of elements in each dimension

arr = np.array([1,2,3])
print(arr.shape)

arr2 = np.array([[1,2,3,4], [5,6,7,7]])
print(arr2.shape)

arr3 = np.array([1,2,3], ndmin=5)
print(arr3.shape)

arr4 = np.array([[1,2,3], [4,5,6]], ndmin=4)
print(arr4.shape)