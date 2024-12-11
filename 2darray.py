from numpy import *
arr=array([[1,2,3,4],[5,6,7,8]])
arr1=full((2,3),7)

print(arr1)
print(arr.ndim)
arr2=arr.flatten()
arr3=arr2.reshape(4,2)
print(arr2)
print(arr3)
