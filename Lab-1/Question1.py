# write a python program that checks if a given integer is divisible by 

num=int(input("Enter a number"))
if (num%3==0 and num%5==0) :
    print("FizzBuzz")
elif(num%3==0):
    print("Fizz")
elif(num%5==0):
    print("Buzz") 
else:
    print (f"The number is {num}")