import numpy as np

arr = np.array([1,2,3])
for x in arr:
    print(x)

arr2 = np.array([[1,2,3], [4,5,6]])
for x in arr2:
    for y in x:
        print(y)


#iterating through nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

for x in np.nditer(arr[:, ::2]):
    print(x)

#ndenumerate
for x in np.ndenumerate(arr):
    print(x)
for idx, x in np.ndenumerate(arr):
    print(idx, x)
