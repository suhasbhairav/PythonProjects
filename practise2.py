import numpy as np

#Array indexing
arr = np.array([1,2,3,4])

print(arr[0])
print(arr[1])

print(arr[2] + arr[3])

print(arr[1] - arr[3])

#Access 2-D arrays
arr_2 = np.array([[1,2,3],[4,5,6]])
print("Accessing 2-D array:", arr_2[0,0])
print(arr_2[0,2])

#Access 3-D arrays
arr_3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

print(arr_3)

print(arr_3[0,1,2])


#negative indexing
arr_negative_indexing = np.array([[1,2,3], [4,5,6]])

print(arr_negative_indexing[1,-1])
print(arr_negative_indexing[1,-2])
print(arr_negative_indexing[0,-1])
print(arr_negative_indexing[0,2])
