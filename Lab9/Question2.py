#Create a CSV file named employees.csv with columns (ID, Name, Salary).
# Write a Python program to insert five  employee records into the file. 
import csv
employee=[
    ["Id","Name","Salary"],
    [1,"Hari",20000],
    [2,"Ram",25000],
    [3,"Sita",18000],
    [4,"Laxman",12000],
    [5,"Gita",30000]
]
with open("Lab9\\employees.csv",'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(employee)
    print("Details written successfully.")