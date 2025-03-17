#Load a dataset from a CSV file, remove duplicate records, and sort the DataFrame by a specific column.
import pandas as pd
data=pd.read_csv("data.csv")
df=pd.DataFrame(data)
#Removing Duplicate Records
duplicated_remove=df.drop_duplicates()
print("Data after droping duplicate reocrds:\n",duplicated_remove[:4])
#Sort the DF by a specific column
sort_data=df.sort_values(by='name',ascending=True)
print("Displaying data according to specific column with sorting:\n",sort_data[:4])