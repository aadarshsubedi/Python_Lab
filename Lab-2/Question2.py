# Calculate the sum of even numbers up to a given number n. 
n=int(input("Enter the n number"))
list=[]
i=1
sum=0
print("Enter the even number")
while i<=n:
    num=int(input())
    sum=sum+num
    i+=2
    
print(f"The sum of even number upto {n} is {sum}")