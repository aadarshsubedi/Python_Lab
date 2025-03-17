# Create a DataFrame using a dictionary containing student names, marks, and subjects. 
# Display the first 5 rows  using the head() function. 
import pandas as pd
Students={
    "Name":["John","Doe","Jane","Doe"],
    "Marks":[90,80,70,60],
    "Subject":["Maths","Science","English","History"]
}
df=pd.DataFrame(Students)
print("Printing the first 5 rows of the DataFrame :")
print(df.head())