def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b
try:  
    def divide(a,b):
        return a/b
except(ZeroDivisionError) as e:
    print("Error: ",e)