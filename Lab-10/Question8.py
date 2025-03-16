#Create a 3x3 matrix with values from 1 to 9. Use broadcasting to add 10 to each row. 
import numpy as np
arr=np.arange(1,10).reshape(3,3)
print("Existing array :",arr)
new_arr=arr+10 # This method is called broadcasting it automatically add 10 without using loop in each element
print("New array :",new_arr)