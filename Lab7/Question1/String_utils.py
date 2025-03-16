#Create a module named string_utils.py with the following functions: 
# reverse_string(s): Returns the reverse of the input string s. 
# count_vowels(s): Returns the number of vowels in the string s. 
# Write a script main.py that imports this module and uses both functions. 

def reverse_string(str):
    return str[::-1]

def count_vowels(str):
    string=str.lower()
    vowels="aeiou"
    count=0
    for s in string:
        if s in vowels:
            count+=1
    return count 

if __name__== '__main__':
    print(count_vowels("Gucci Gang"))