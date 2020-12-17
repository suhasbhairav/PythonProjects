import numpy as np

#Array slicing
arr = np.array([1,2,3,4,5])
print(arr[1:3])
print(arr[:2])
print(arr[1:])
print(arr[0:4:2])

#Negative slicing
print(arr[0:-2])

print(arr[::2])

#Slicing 2-D arrays
arr2 = np.array([[1,2,3], [4,5,6]])

print(arr2[1, 0:2])
print(arr2[0, 0:1])

#From both elements return index 1
print(arr2[0:2, 1])

print(arr2[0:2, 0:1])