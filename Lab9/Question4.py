# Write a Python program to create a new directory named MyFiles using the os module.
import os
dir="MyFiles"
try:
    os.mkdir(dir)
    print(f"{dir} name directory is created")
except Exception as e:
    print("Error:",e)
    