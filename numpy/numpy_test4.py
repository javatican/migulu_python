import numpy as np  
arr1 = np.arange(10)
print(arr1)
print(arr1[6])
print(arr1[4:6])
arr1[3:6]=100
print(arr1)
arr2=arr1[5:8]
print(arr2)
arr2[1]=50
print(arr1)
arr2[:]=200
print(arr1)
#copy()
arr3=arr1[1:4].copy()
print(arr3)
arr3[1]=500
print(arr3)
print(arr1)

