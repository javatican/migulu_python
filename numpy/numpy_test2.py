import numpy as np 
arr1 = np.zeros(10)
print(arr1) 
print(arr1.dtype) 
arr2 = np.ones((5,4))
print(arr2) 
print(arr1.dtype) 
arr3 = np.empty((3,2))
print(arr3) 
print(arr1.dtype) 
arr4=np.arange(12)
print(arr4) 
print(arr4.dtype) 
arr5 = np.ones_like(arr3)
print(arr5) 
print(arr5.dtype) 
arr6=np.identity(5)
print(arr6) 
print(arr6.dtype) 
arr7=arr1.astype(np.int64)
print(arr7)
data2=[1.2,2.3,9.01,8.99,4.5,0.67]
arr8=np.array(data2)
arr9=arr8.astype(np.int64)
print(arr9)