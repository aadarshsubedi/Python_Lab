#Create a NumPy array of numbers from 1 to 20. Extract the even numbers using slicing and indexing. 
import numpy as np
arr=np.arange(1,21)
even_num=arr[1::2]
print("The even numbers :",even_num)