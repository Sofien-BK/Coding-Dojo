class Bank_account():
    def __init__(self, intii_rate, balance=0):
        self.balance = balance
        self.intii_rate=intii_rate
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Your balance has increased {amount} $\nYour balance now is {self.balance} $')
        return self
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print(f'You have withdraw {amount} $\nYour balance now is {self.balance}  $')
        elif self.balance<=amount:
            self.balance = self.balance-5
            print(f'Insufficient funds: Charging a $5 fee\nYour balance now is {self.balance} $')
        return self
    def display_account_info(self):
        print(f'Balance: {self.balance} $')
        return  self
    def yield_interest(self):
        self.balance += (self.balance*self.intii_rate)
        print(f'Your balance increased by the interest rate: {self.intii_rate}\nYour balance now is {self.balance} $')
        return self

