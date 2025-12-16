# Using encapsulation 
class BankAccount:
    def __init__(self, balance):
        self.__balance= balance  

    def deposit(self, amount):
         self.__balance += amount
         
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient amount!")    

    def get_balance(self):
        return self.__balance

amount = int(input("Enter the amount: "))
acc = BankAccount(amount)
 
print("Choose the options\n1. deposit\n2. withdraw")
choose = (input("Enter the choice: "))

if choose=="1":
    deposit_amount = int(input("Enter the deposit amount: "))
    acc.deposit(deposit_amount)
    
elif choose=="2":
    withdraw_amount = int(input("Enter the withdraw ammount: "))
    acc.withdraw(withdraw_amount) 
else:
    print("invalid choice!")

print("Current Balance: ",acc.get_balance())
