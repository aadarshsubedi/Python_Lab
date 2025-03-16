# Write a function that takes variable number of arguments and returns their sum.
def Sum(*args):
    return sum(args)

print(f"The sum of two number is {Sum(1,2,3,4,5,6)}")