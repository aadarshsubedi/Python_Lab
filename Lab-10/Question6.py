#Create an array using arange() from 10 to 100 with a step size of 10. Convert it into a 3x3 matrix.
import numpy as np
arr=np.arange(10,100,10)
new_arr=arr.reshape(3,3)
print(new_arr)