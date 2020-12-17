import numpy as np

arr = np.array([1,2,3])
print(arr)

arr2 = np.array(["dog", "cat", "cow"])
print(arr2)

arr3 = np.array([1, 2.3, 5.8])
print(arr3)

arr4 = np.array([1,2,3,4], dtype='S')
print(arr4)

#Float to integer

arr5 = np.array([1.2, 2.3, 3.4])
arr6 = arr5.astype('i')

print(arr6)

arr7 = np.array([1.4, 3.5, 8.9])
arr8 = arr7.astype('i')
print(arr8)

arr9 = arr7.astype(int)
print(arr9)

arr10 = np.array([1,0,3, -1])
print(arr10.astype(bool))