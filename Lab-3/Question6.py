#Create a lambda function to compute the cube of a number.
x=int(input("Enter the number you want to cube"))
value=lambda x: x**3

print(f"The cube is {value(x)}")