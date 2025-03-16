#Keep asking the user for input until they enter a number between 1 and 10. 
num=int(input("Enter the number between 1 to 10"))
while(1):
    
    if num>=1 and num<=10 :
        break
    else:
        num=int(input("Enter the number inbetween 1 and 10  "))