import encrypt_decrypt

class User:
    def __init__(self, name, username, password):
        self.user = name
        self.username = username
        self.password_hash = password

    def get_user(self, name):
            return self.user
    

class Account(User):
    def __init__(self, name, username, password, checking = 0, saving = 0):
        username = encrypt_decrypt.encrypt(username)
        password =  encrypt_decrypt.encrypt(password)

        User.__init__(self, name, username, password)
        self.checking_balance = encrypt_decrypt.encrypt(checking)
        self.savings_balance =  encrypt_decrypt.encrypt(saving)
       

    def deposit(self, type, amount):
        if type == 'checking':
            self.checking_balance = encrypt_decrypt.decrypt(self.checking_balance)
            self.checking_balance = self.checking_balance + amount
            self.checking_balance = encrypt_decrypt.encrypt(self.checking_balance)
        elif type == 'savings':
            self.checking_balance = encrypt_decrypt.decrypt(self.checking_balance)
            self.savings_balance = self.savings_balance + amount
            self.checking_balance = encrypt_decrypt.encrypt(self.checking_balance)
        else:
            print('Invalid Balance Type')

    def withdraw(self, type, amount):
        if type == 'checking':
            self.checking_balance = encrypt_decrypt.decrypt(self.checking_balance)

            if amount > self.checking_balance:
                print('Insufficient Funds in Checking Account')
            else:
                self.checking_balance = self.checking_balance - amount
                print("$" + str(amount) + " withdrawn from checking account")

            self.checking_balance = encrypt_decrypt.encrypt(self.checking_balance)
        elif type == 'savings':
            self.savings_balance = encrypt_decrypt.decrypt(self.savings_balance)

            if amount > self.savings_balance:
                print('Insufficient Funds in Savings Account')
            else:
                self.savings_balance = self.savings_balance - amount
                print("$" + str(amount) + " withdrawn from savings account")
            
            self.savings_balance = encrypt_decrypt.encrypt(self.savings_balance)
        else:
            print('Invalid Balance Type')
    
    def view_balance(self, type):
        if type == 'checking':
            self.checking_balance = encrypt_decrypt.decrypt(self.checking_balance)
            print('$' + str(self.checking_balance))
            self.checking_balance = encrypt_decrypt.encrypt(self.checking_balance)
        elif type == 'savings':
            self.savings_balance = encrypt_decrypt.decrypt(self.savings_balance)
            print('$' + str(self.savings_balance))
            self.savings_balance = encrypt_decrypt.encrypt(self.savings_balance)
        else:
            print('Invalid Balance Type')