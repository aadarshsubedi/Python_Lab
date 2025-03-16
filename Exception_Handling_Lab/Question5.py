#Write a program that asks the user to input their age. Handle the following exceptions: • 
# If the user enters a non-numeric value, catch the ValueError. 
#• If the user enters an age less than 0 or greater than 120, raise a custom exception InvalidAgeError.
# • Print a message if the age is valid. 
class InvalidAgeError(Exception):
    pass

try:
    age=int(input("Enter the age"))
    if age<0 or age>120:
        raise InvalidAgeError("The age is Invalid")
    else:
        print(f"The valid age is {age}")
    
except(ValueError,InvalidAgeError) as e:
    print("The error is ",e)