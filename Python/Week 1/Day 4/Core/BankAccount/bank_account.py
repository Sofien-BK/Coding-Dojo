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

adamsAccount=Bank_account(0.1,1200)
juliasAccount=Bank_account(0.3,5600)
adamsAccount.deposit(300).deposit(578).deposit(758).withdraw(1769).yield_interest().display_account_info()
juliasAccount.deposit(781).deposit(1415).withdraw(964).withdraw(3154).withdraw(75).withdraw(770).yield_interest().display_account_info()

