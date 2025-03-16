# Write a Python program to count the number of words in a text file. 
with open("sample.txt","r") as f:
    count=0
    content=f.read()
    content=content.split()
    count+=len(content)
    print(f"The number of words in text file: {count}")
    