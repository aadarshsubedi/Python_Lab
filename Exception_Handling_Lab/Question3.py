"""Write a program that asks the user to input a list of numbers and calculates the average. Handle the following  exceptions: 
• If the user enters a non-numeric value, catch the ValueError. 
• If the list is empty, raise a custom exception called EmptyListError. 
• Print the average if no exceptions occur """
class EmptyListError(Exception):
     pass

try:
    num=[]
    n=int(input("Enter the length of list"))
    print("Enter a list of number")
    for i in range(n):
        n=int(input())
        num.append(n)
    if not list:
        raise EmptyListError("Enter the value in list")
    else:
        sum=sum(num)
        print(f"The average of the list number is {sum/n}")
        
except(ValueError,EmptyListError) as e:
    print("The error message is ",e)