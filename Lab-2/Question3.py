#Print the multiplication table for a given number up to 10, but skip the fifth iteration.
n=int(input("Enter the number which multiplication you want"))
for x in range(1,10+1):
    if(x==5):
        continue
    print(f"{n} * {x} = {n*x}")
