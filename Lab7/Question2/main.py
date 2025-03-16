"""2. Create a package named calculator with the following modules: 
basic_operations.py: Contains functions add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
advanced_operations.py: Contains functions power(a, b) and sqrt(a). 
 Write a script main.py that imports the calculator package and uses all the functions. 
"""
from Calculator import basic_operations as b,advanced_operations as a

print("Addition: ",b.add(10,15))
print("Subtraction: ",b.subtract(35,12))
print("Multiplication: ",b.multiply(5,9))
print("Division: ",b.divide(24,8))

print("Power: ",a.power(3,2))
print("Square Root: ",a.sqrt(36))