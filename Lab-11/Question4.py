#Load a dataset from a CSV file into a Pandas DataFrame. Display the last 5 rows using the tail() function. 
import pandas as pd
df = pd.read_csv('data.csv')

# Display the last 5 rows
print(df.tail(5))