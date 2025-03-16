#  Write a Python program to remove all blank lines from a text file.
with open("sample.txt", "r") as f:
    lines = f.readlines()  # Read all lines

# Write back only non-empty lines
with open("sample.txt", "w") as f:
    f.writelines(line for line in lines if line.strip())  

print("Blank lines removed!")