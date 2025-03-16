# Write a Python script that checks whether a file named data.txt exists in the current directory and prints an  appropriate message. 
import os
try:
    if os.path.exists("data.txt"):
        print("File name data.txt exist")
    else:
        raise FileNotFoundError("File doesnot exist in Directory")
except FileNotFoundError as e:
    print("Error: ",e)