#Given a string, find the first non-repeated character. 
from collections import Counter

def first_non_repeated_char(s):
    char_count = Counter(s)  # Count occurrences of each character
    for char in s:  # Iterate through the string
        if char_count[char] == 1:
            return char  # Return the first non-repeated character
    return None  # Return None if all characters are repeated

# Example usage
string = "aadarsh"
print(f"The first non repeated character is {first_non_repeated_char(string)}")