# Write a Python program to count the number of lines in a text file. 
with open("sample.txt","r") as f:
    count=len(f.readlines())
    print(f"The number of lines in text: {count}")