#Read a CSV file into a DataFrame, modify the data (e.g., add a new column), and save it back to a new CSV file. 
import pandas as pd
data=pd.read_csv("data.csv")
df=pd.DataFrame(data)
print("Existing csv data:\n",df[:4])
df['Id']=range(101,len(df)+101)
print("Details after adding new column: \n",df[:4])
df.to_csv("new_data.csv",index=False)
print("Data has been save successfully into new csv file")