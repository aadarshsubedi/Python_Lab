# Write a Python program to find and replace a specific word in a text file. 
with open("sample.txt","r") as f:
    content=f.read()
find_word=input("Enter the word you want to find: ")
replace_word=input("Enter the word you want to replace: ")
if find_word in content:
    content=content.replace(find_word,replace_word)
    with open("sample.txt","w") as f:
        f.write(content)
        print("The word is replace.")
else:
    print("There is no such word")

    
    