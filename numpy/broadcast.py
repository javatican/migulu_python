import numpy as np
arr1=np.random.rand(4,3)
print(arr1)
mean=arr1.mean(0)
print(mean)
arr2=arr1-mean
print(arr2)
print(arr2.mean(0))
#
mean2=arr1.mean(1).reshape(4,1)
print(mean2)
print(mean2.shape)
arr3=arr1-mean2
print(arr3.mean(1))