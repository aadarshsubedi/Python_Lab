#Write a function multiply that multiplies two numbers, but can also accept and multiply strings. 
def Multiply(a,b):
    if isinstance(a,str) and isinstance(b,int):
        print(a * b)
    elif isinstance(b,str) and isinstance(a,int):
        print(a * b)
    elif isinstance(a,int) and isinstance(b,int):
        print(a * b)
    else:
        print("Invalid input types")
Multiply(12,3)
Multiply(3,"Aadarsh")
