#Create a custom exception called NegativeNumberError. Write a program that asks the user to input a positive  integer. 
# If the user enters a negative number, raise the NegativeNumberError and handle it.
class NegativeNumberError(Exception):
    pass

try:
    n=int(input("Enter the positive integer"))
    if(n<0):
        raise NegativeNumberError("Negative Integer")
    else:
        print("The positive integer is ",n)
except(NegativeNumberError) as e:
    print("The error is ",e)