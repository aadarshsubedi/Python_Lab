#Differentiate between copy and view in NumPy by modifying a view and observing changes in the original array. 
import numpy as np
arr=np.arange(1,10).reshape(3,3)
brr=arr.copy() # It will copy the content of the arr array into different memory
print("Content of arr",arr)
brr[1,2]=23
print("Content of arr after value interchange in brr using copy :",arr)
crr=arr.view() # View will take the address of the arr and any change in crr will change the arr
crr[2,0]=99
print("Content of arr after value interchange in crr using view :",arr)