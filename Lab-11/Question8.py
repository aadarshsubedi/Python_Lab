#Perform an inner join and left join on two DataFrames containing student details and exam scores.
import pandas as pd
data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [20, 21, 19, 22, 20]
}
data2 = {
    'ID': [1, 2, 3, 6, 7],
    'Score': [85, 90, 78, 88, 76]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
inner_join=pd.merge(df1,df2,how='inner')
left_join=pd.merge(df1,df2,how='left')
print("Inner Join: \n",inner_join)
print("Left Join: \n",left_join)