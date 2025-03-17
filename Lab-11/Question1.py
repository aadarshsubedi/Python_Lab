# Create a Pandas Series from a Python list and a NumPy array. Display the index, values, and data type of the  Series. 
import pandas as pd
import numpy as np
pd_series= pd.Series([1,2,3])
np_array=np.array([4,5,6])
print("Printing the Pandas Series :")
for index,value in pd_series.items():
    print(f"Index: {index}  Value: {value}  Data Type: {type(value)}")

print("Printing the Numpy Array :")
for index,value in enumerate(np_array) :
    print(f"Index: {index}  Value: {value}  Data Type: {type(value)}")