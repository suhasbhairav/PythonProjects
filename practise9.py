import numpy as np

# Array joining
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 4, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([2, 3, 4])
arr = np.concatenate((arr3, arr4))
print(arr)

# 2-D arrays along axis 1
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 3], [4, 5]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr)

# Stacking is same as concatenation, the only difference is that stacking is done along a new axis. - W3SCHOOLS
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# To stack along rows
arr = np.hstack((arr1, arr2))
print(arr)

# To stack along columns
arr = np.vstack((arr1, arr2))
print(arr)

# To stack along height
arr = np.dstack((arr1, arr2))
print(arr)
