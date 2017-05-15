import numpy as np  
data1=[[1.2,2.3,9.01],[8.99,4.5,0.67],[3.4,1.2,8.2],[6.9,9.4,3.7]] 
arr1 = np.array(data1)
print(arr1)
# ndarray and scalar
arr2 = arr1*10 
print(arr2)
arr3 = arr1**0.5 
print(arr3)
# between ndarray
arr4=arr1*arr1
print(arr4)
arr5=arr1+arr4
print(arr5)
