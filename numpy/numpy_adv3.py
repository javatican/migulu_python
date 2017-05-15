import numpy as np  
arr1 = np.arange(35).reshape(5,7)
print(arr1)
arr2=arr1[np.array([0,2,4]), np.array([0,1,2])]
print(arr2)