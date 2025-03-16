#Write a Python program to read a CSV file named data.csv and print its contents row by row. 
import csv

with open("Lab9\\data.csv",mode="r",newline='') as f:
    content=csv.reader(f)
    for row in content:
        print (row)