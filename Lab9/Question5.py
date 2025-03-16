#Write a Python program to list all files and directories in the current working directory using the os module 
import os 
cur_dir=os.getcwd()
items=os.listdir(cur_dir)
print("The current Directories content: ")
for item in items:
    print(item)