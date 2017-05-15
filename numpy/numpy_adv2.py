import numpy as np  
arr1=np.arange(10,1,-1)
print(arr1)
arr2=arr1[np.array([1,3,2,1])]
print(arr2)
arr3=arr1[np.array([[1,5],[2,6]])]
print(arr3)
arr3[0,0]=100
print(arr3)
print(arr1)