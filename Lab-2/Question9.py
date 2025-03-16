#Check if all elements in a list are unique.
# If a duplicate is found, exit the loop and print the duplicate. items = ["apple", "banana", "orange", "apple", "mango"] 
list=["apple", "banana", "orange","apple", "mango"]
dup=set()
for item in list:
    if item in dup:
        print(f"The duplicate item is {item}")
        break
    dup.add(item)
else: 
    print("All the elements are unique")