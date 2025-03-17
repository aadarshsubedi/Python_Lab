#Convert a float NumPy array into an integer array using .astype().
import numpy as np
arr=np.array([[12.1,15.5,20.1],[99.99,69.69,55.55]])
print("Existing data type of array :",arr.dtype)
new_arr=arr.astype('i')
print("New data type of array :",new_arr.dtype)
print(new_arr)