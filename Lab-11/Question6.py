#Given a DataFrame with columns (Product, Price, Quantity), perform the following: o Select only the Price column. 
# o Retrieve the first 3 rows using slicing. 
# o Filter and display products where the price is greater than 500. 
import pandas as pd
data = { 
 'Product': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Printer'], 
 'Price': [1200, 800, 300, 450, 600], 
 'Quantity': [10, 15, 20, 5, 8] 
} 

df=pd.DataFrame(data)
#Selecting only the price column
print("Selecting the Price Column: \n",df['Price'])

#Selecting the first 3 rows
print("Selecting the First 3 rows:\n",df[:3])

#Filtering products which is greater than 500
filter_price=df[df['Price']>500]
print("Product whose price is greater than 500: \n",filter_price)

