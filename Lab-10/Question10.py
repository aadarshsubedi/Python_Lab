#. Generate a random NumPy array of 15 elements between 1 and 100. 
# Sort the array in ascending order. 
# Find the index of the maximum and minimum values. 
import numpy as np
arr=np.random.randint(1,101,15)
print("Random Value of 15 element: ",arr)
print("The minimum value index :",np.argmin(arr))
print("The maximum value index :",np.argmax(arr))
arr=np.sort(arr)
print("Sorted Value in ascending order :",arr)
