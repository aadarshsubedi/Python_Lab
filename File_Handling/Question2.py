#Write a Python program to read and display the content of "sample.txt". 
with open("sample.txt","r") as f:
    content=f.read()
    print(f"The content of the file: {content}")
    