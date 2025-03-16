# Write a Python program to read a file and count the number of occurrences of a specific word.
word = input("Enter a word: ").strip().lower()
count = 0
with open("sample.txt", "r") as f:
    for line in f:
        words = line.lower().split()
        count += words.count(word) 
    print("Occurence of word: ", count)