#Write a Python program to search for a specific record in a CSV file (e.g., search for an employee by ID in  employees.csv). 
import csv
id=int(input("Enter the employee Id you want to search"))
with open("Lab9\\employees.csv",'r',newline='') as file:
    content=csv.reader(file)
    next(content)
    for row in content:
       if row and row[0]== str(id) :
           print(f"ID: {row[0]} Name: {row[1]} Salary: {row[2]}")
           break
    else:
           print("ID doesnot exist")
        