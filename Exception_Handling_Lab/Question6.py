""" Write a program that simulates a login system. Ask the user to input their username and password.
 Handle the  following exceptions: 
• If the username is empty, raise a custom exception EmptyUsernameError. 
• If the password is less than 8 characters, raise a custom exception WeakPasswordError. 
• If the username or password is incorrect, raise a custom exception InvalidCredentialsError. """
class WeakPasswordError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass
class EmptyUserNameError(Exception):
    pass
VALID_USERNAME="Aadarsh"
VALID_PASSWORD="12345678"
try:
    un=input("Enter the username:")
    pw=input("Enter the password:")
    if not un:
        raise EmptyUserNameError("Username is empty")
    elif len(pw)<8:
        raise WeakPasswordError("Password is weak")
    elif un!=VALID_USERNAME or pw!=VALID_PASSWORD:
        raise InvalidCredentialsError("Invalid username or password")
    else:
        print(f"The username {un} and password {pw} is valid ")
    
except(EmptyUserNameError,WeakPasswordError,InvalidCredentialsError) as e:
    print("The error:",e)