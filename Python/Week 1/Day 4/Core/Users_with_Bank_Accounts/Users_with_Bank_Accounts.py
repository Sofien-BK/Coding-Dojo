from bank_account import Bank_account


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bank_account(intii_rate=0.02, balance=0)

    # other methods

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info
        return self    



