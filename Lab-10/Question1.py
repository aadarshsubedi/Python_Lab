#  Write a Python program to create a NumPy array from a given list. 
# Display its type, shape, and dimensions. given_list = [1, 2, 3, 4, 5] 
import numpy as np
arr= np.array([1,2,3,4,5])
print("The type of array :",type(arr))
print("The shape of array :",arr.shape)
print("The dimensions :",arr.ndim)