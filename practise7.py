import numpy as np

#reshape from 1D to 2D

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)

print(newarr.shape)

#1D to 3D
newarr2 = arr.reshape(2, 3, 2)
print(newarr2.base)

print(newarr2.shape)

newarr3 = arr.reshape(2,3,-1)
print(newarr3.shape)

#Flattening an array - Converting multi-dimensional arrays t0 1-D arrays
newarr4 = arr.reshape(-1)
print(newarr4)