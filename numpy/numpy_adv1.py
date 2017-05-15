import numpy as np  
arr1=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr1)
v1 = arr1[1]
print(v1)
v1[1]=100
print(arr1)
print(arr1[1][1])
print(arr1[1, 1])
v2 = arr1[:2]
print(v2)
print(v2.shape)
v3 = arr1[:2,1:]
print(v3)
print(v3.shape)
v4 = arr1[: ,2:]
print(v4)
print(v4.shape)
v5 = arr1[: ,2]
print(v5)
print(v5.shape)
v6 = arr1[2,1:]
print(v6)
print(v6.shape)