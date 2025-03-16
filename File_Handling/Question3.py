#Write a Python program to append the text "Appended Line." to an existing file.
with open("sample.txt","a") as f:
    string="\nAppend Line"
    f.write(string)
    print("File append successfully")