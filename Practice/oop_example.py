class Account:
    def __init__(self, name, balance1=0):
        self.name = name
        self.balance1 = balance1

    def withdraw(self):
        self.balance1 += self.balance1
        print('Account withdrawn')

    def deposit(self, amount):
        self.balance1 = self.balance1 + amount
        print('Account deposited')

oba = Account("oba", 1500)



oba = Account("oba", 1500)
oba.withdraw()
print(oba.balance1)
oba.deposit(1500)
print(oba.balance1)