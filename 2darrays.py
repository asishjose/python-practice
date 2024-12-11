import numpy as np

class Arr:
    def getArray(self):
        array1=np.array([[10,20,30],[40,50,60]])
        array2=np.array([[1,2,3],[4,5,6]])
        return array1,array2
    def addArray(self,array1,array2):
        result = array1 + array2
        return result
    def displayArray(self,res):
        print(res)

if __name__=='__main__':
    a=Arr()
    arr1,arr2=a.getArray()
    result=a.addArray(arr1,arr2)
    a.displayArray(result)

