# Create a Pandas DataFrame using a dictionary with at least three columns (e.g., Name, Age, Salary). 
# Print its attributes like shape, size, columns, and dtypes. 
import pandas as pd
Dictionary={
    "Name":["John","Doe","Jane","Doe"],
    "Age":[21,32,24,20],
    "Salary":[20000,25000,19000,30000]
}
pf=pd.DataFrame(Dictionary)
print("Shape: ",pf.shape)
print("Size: ",pf.size)
print("Columns: ",pf.columns)
print("Data Type: \n",pf.dtypes)