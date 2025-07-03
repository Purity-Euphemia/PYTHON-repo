class Account:
    def __init__(self, name, balance1=0):
        self.name = name
        self.balance1 = balance1

    #def st_value(self, value):
       # self.name - value

    def get_name(self):
        return self.name

    def sef_balance(self, amount):
        if amount < 0:
            raise ValueError('amount cannot be negative')
        self.balance = amount


    def get_balance(self):
        return self.balance1

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