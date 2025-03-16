#1. Write a Python program to create a text file named "sample.txt" and write the sentence "Hello, this is a sample  file." into it. 
with open("sample.txt","w") as f:
    content="Hello,this is a sample file."
    f.write(content)
    print("Content is written successfully in file")
    