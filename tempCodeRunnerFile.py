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
acc.withdraw(amount)