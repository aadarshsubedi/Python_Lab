#Write a Python program to rename a file from old_name.txt to new_name.txt using the os module. 
import os
try: 
   if os.path.exists("dissample.txt"):
        os.rename("dissample.txt","sample.txt")
        print("File renamed successfully")
   else:
       raise FileNotFoundError("File doesnot exist")
except FileNotFoundError as e:
    print("Error: ",e)
