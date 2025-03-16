#Create an abstract class Account with abstract methods deposit(), 
# withdraw(), and check_balance(). Derive  two classes SavingsAccount and CurrentAccount and implement the methods. 
from abc import ABC, abstractmethod 

class Account(ABC):
    def __init__(self, balance=0):
        self.balance = balance 
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"Savings Account: Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Savings Account: Withdraw {amount}, New Balance: {self.balance}")
        else:
            print("Not enough balance in Savings Account.")

    def check_balance(self):
        print(f"Savings Account Balance: {self.balance}")

class CurrentAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"Current Account: Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Current Account: Withdrew {amount}, New Balance: {self.balance}")
        else:
            print("Not enough balance in Current Account.")

    def check_balance(self):
        print(f"Current Account Balance: {self.balance}")

s = SavingsAccount(1000)  
c = CurrentAccount(2000)  

s.deposit(500)
s.withdraw(300)
s.check_balance()

c.deposit(1000)
c.withdraw(5000)  
c.check_balance()