class User:
    def __init__(self, name, password):
        self.username = name
        self.password_hash = password

class Account(User):
    def __init__(self, name, password):
        User.__init__(self, name, password)
        self.checking_balance = 0
        self.savings_balance = 0
    

    def deposit(self, type, amount):
        if type == 'checking':
            self.checking_balance = self.checking_balance + amount
        elif type == 'savings':
            self.savings_balance = self.savings_balance + amount
        else:
            print('Invalid Balance Type')

    def withdraw(self, type, amount):
        if type == 'checking':
            if amount > self.checking_balance:
                print('Insufficient Funds in Checking Account')
            else:
                self.checking_balance = self.checking_balance - amount
                print("$" + str(amount) + " withdrawn from checking account")
        elif type == 'savings':
            if amount > self.savings_balance:
                print('Insufficient Funds in Savings Account')
            else:
                self.savings_balance = self.savings_balance - amount
                print("$" + str(amount) + " withdrawn from savings account")
        else:
            print('Invalid Balance Type')
    
    def view_balance(self, type):
        if type == 'checking':
            print('$' + str(self.checking_balance))
        elif type == 'savings':
            print('$' + str(self.savings_balance))
        else:
            print('Invalid Balance Type')
