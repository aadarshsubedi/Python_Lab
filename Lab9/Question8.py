#Write a Python script to delete a file named temp.txt and confirm its deletion.
import os

try: 
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
        print("File delete successfuly")
        print("After the Deletion.....")
        if os.path.exists("temp.txt"):
            print("File doesnot delete")
        else:
            raise FileNotFoundError("It is confirm file is delete")
    else:
        raise FileNotFoundError("File doesnot exist")
except FileNotFoundError as e:
    print("Error: ",e)