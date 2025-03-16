# A company gives a discount based on the following conditions:
#Purchase amount greater than $10000: 20% discount
# Purchase amount between $5000 and $10000:10% discount
# Purchase amount less than $5000: No discount
#Write a Python program to calculate the final price after applying the discount.
# amount=int(input("Enter the amount:"))


#     if amount > 10000 :
#         amount= amount-amount*0.2
#         print(f"The total purchase amount is {amount}")
        
#     elif amount>5000 :
#         amount=amount-amount*0.1
#         print(f"The total purchase amount is {amount}")
        
#     else:
#         print(f"The purchase amount is {amount}")
amount = int(input("Enter the purchase amount: "))

if amount > 10000:
    amount -= amount * 0.2 
    print(f"The total purchase amount after discount is ${amount}")
elif amount > 5000:
    amount -= amount * 0.1
    print(f"The total purchase amount after discount is ${amount}")
else:
    print(f"The total purchase amount is ${amount}")