# Create a 3D NumPy array with shape (2, 3, 4). Access the second row of the first matrix using slicing.
import numpy as np
arr=np.arange(1,25).reshape(2,3,4)#arange will give the number from 1 to 24 and reshape will shape the number into the given matrix
second_row=arr[0,1,:]
print("The element of first matrix second row :",second_row)