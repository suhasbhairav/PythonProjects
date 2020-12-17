import numpy as np

arr = np.array([1,2,3,4,5])

arr1 = np.array([10, 20, 30, 40, 50])
print(arr1)

arr2 = np.array([15, 20, 25, 30, 35])

print(arr2)

print(arr)


tup = np.array((1,2,3,4,5))

tup1 = np.array((10,20,30,40,50))
print(tup1)
print(tup)

#0-D arrays
zero_arrays = np.array(42)
print((zero_arrays))

#1-D arrays

one_arrays = np.array([1,2,3,4,5])
print(one_arrays)

#1-D arrays
one_d_arrays = np.array([10,20,30,40,50])
print(one_d_arrays)

#2-D arrays
two_d_arrays = np.array([[1,2,3], [4,5,6]])
print(two_d_arrays)

#2-d arrays
two_d_arr2 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
print(two_d_arr2)

#3-D arrays
three_d_arrays = np.array([[[1,2,3],[3,4,5]], [[1,2,4], [5,6,7]]])
print(three_d_arrays)

print(three_d_arrays.shape)


arr10 = np.array([1,2,3,4,5])
print(arr10)


#0-D array
arr0 = np.array(100)
print(arr0)


#1-D
one_dimension_arr = np.array([1,2,3,4,5,6])

print(one_dimension_arr)

#2-D arrays
two_dimension_arr = np.array([[1,2,3,4],[5,6,7,8]])
print(two_dimension_arr)

#3-D arrays
three_dimension_arr = np.array([[[1,2,3],[4,5,6]], [[1,2,3], [4,5,6]]])
print(three_dimension_arr)

#3-d arrays
three_d_arrs = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]])
print(three_d_arrs)

#Check dimensions
print(arr0.ndim)

print(one_dimension_arr.ndim)

print(two_dimension_arr.ndim)
print(three_dimension_arr.ndim)
print(three_d_arrs.ndim)

#Creating higher dimensional arrays
five_dimension_arrs = np.array([1,2,3,4,5], ndmin=5)
print(five_dimension_arrs)
print("Arr", five_dimension_arrs.ndim)

#Six dimension
six_dimension_arr = np.array([1,2,3], ndmin=6)
print(six_dimension_arr)
print("Dimension:", six_dimension_arr.ndim)





