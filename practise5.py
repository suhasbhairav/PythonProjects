import numpy as np

#Copy vs View

#Copy - deep copy
arr = np.array([1,2,3])
arr2 = arr.copy()
arr2[0]= 10
print(arr)
print(arr2)

arr1 = np.array([10,20,30])
arr3 = arr1.copy()
arr1[0]= 100
print(arr1)
print(arr3)


#View- Shallow copy
arr4 = np.array([1,2,3])
arr5 = arr4.view()

arr4[1] = 200
print(arr4)
print(arr5)

arr5[1] = 300
print(arr4)
print(arr5)

#Check if array owns the data - this is done using base
print(arr2.base)
print(arr5.base)


