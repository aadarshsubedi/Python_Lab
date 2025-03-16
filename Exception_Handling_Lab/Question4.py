#Write a program that asks the user to input a number between 1 and 10. If the user enters a number outside this  range, 
# raise a ValueError and allow the user to retry up to 3 times.
# If the user fails to enter a valid number after 3  attempts, print an error message.

def Num_Of_Attempt():
    attempt=3
    for x in range(attempt):
            try:
                n=int(input("Enter the number in between range 1 to 10"))
                if n<0 or n>10:
                   raise ValueError("The value is out of range")
                print("The valid number is ",n) 
                return n
            except(ValueError) as e:
                print(f"Error: {e}")
                print(f"Attempts remaining: {attempt - x - 1}")
    print("Too many attempts. Exiting the process....")
    

Num_Of_Attempt()
        