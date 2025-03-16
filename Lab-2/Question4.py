#Reverse a string using a loop. 
str=input("Enter a string")
x=len(str)-1
list=[]
while x>=0:
    list.append(str[x])
    x-=1

print(f"The reverse of string is {list}")