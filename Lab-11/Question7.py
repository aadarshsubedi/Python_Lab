# Create two DataFrames: 
# o df1 with columns (ID, Name, Age) 
# o df2 with columns (ID, Salary, Department) 
# o Merge these DataFrames on the "ID" column and display the result. 
import pandas as pd
data1={
    'Id':[101,102,103,104],
    'Name':["Joe","Mick","Jully","David"],
    'Age':[21,43,25,30]
}
data2={
    'Id':[101,102,103,104],
    'Salary':[20000,15000,35000,23000],
    'Department':["IT","HR","Finance","Project"]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
merge_details=pd.merge(df1,df2,how="inner",on='Id')
print("Merge Details: \n",merge_details)