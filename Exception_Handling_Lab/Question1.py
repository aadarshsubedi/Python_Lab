""" Write a Python program that asks the user to input two numbers and performs division. Handle the following  exceptions: 
• If the user enters a non-numeric value, catch the ValueError. 
• If the user tries to divide by zero, catch the ZeroDivisionError. 
• Print a meaningful message for each exception.  """

try: 
    n1=int(input("Enter the first number"))
    n2=int(input("Enter the second number"))
    c=n1/n2
    print(f"The division of {n1} and {n2} is {c}")
    
except(ZeroDivisionError,ValueError) as e:
    print("The error message is ",e)
    
    