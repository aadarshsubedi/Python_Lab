#Check if a number is prime. 
num=int(input("Enter a number"))
count=0
if num==2 or num==1:
    print("It is a prime number")

else :
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    
if(count==2):
    print(f"The {num} is a prime number")
    
else:
    print(f"The {num} isnot a prime number")
    