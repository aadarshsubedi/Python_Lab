#8. Create a function that accepts any number of keyword arguments and prints them in the format key: value.
def Multi_Value(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        

Multi_Value(Brand="BMW",Model="BMW M2",Manufacture=1998)