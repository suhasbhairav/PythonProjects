import numpy as np

arr = np.array([1,2,3,4,5,6])
x = np.where(arr == 4)
print(x)

x = np.where(arr == 100)
print(x)

x = np.where( arr%2 == 1)
print(x)

x = np.searchsorted(arr, 4.5)
print(x)

x = np.searchsorted(arr, 4, side='right')
print(x)

x = np.searchsorted(arr, [1,5])
print(x)