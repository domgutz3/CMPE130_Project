import encrypt_decrypt

#tested all functions 
class User:
    def __init__(self, name, username, password):
        self.user = name
        self.username = username
        self.password_hash = password

    def setName(self, name):
        self.user = name 
    
    def setUsername(self, username):
        self.username = encrypt_decrypt.encrypt(username)
    
    def setPassword(self, password):
        self.password_hash = encrypt_decrypt.encrypt(password) 

    def getUser(self):
        return self.user

    def getUsername(self):
        return encrypt_decrypt.decrypt(self.username)
    
    def getPassword(self):
        return encrypt_decrypt.decrypt(self.password_hash)
    
    def printInfo(self):
        print("Name: ", self.user)
        print("Username: ", encrypt_decrypt.decrypt(self.username))
        print("Password: ", encrypt_decrypt.decrypt(self.password_hash))

class Account(User):
    def __init__(self, name, username, password, checking = 0.00, saving = 0.00):
        username = encrypt_decrypt.encrypt(username)
        password =  encrypt_decrypt.encrypt(password)

        User.__init__(self, name, username, password)
        self.checking_balance = encrypt_decrypt.encrypt(checking)
        self.savings_balance =  encrypt_decrypt.encrypt(saving)
       
    def setChecking(self, checking):
        self.checking_balance = encrypt_decrypt.encrypt(self.checking_balance)

    def setSavings(self, saving):
        self.savings_balance = encrypt_decrypt.encrypt(self.savings_balance) 

    def getChecking(self):
        return encrypt_decrypt.decrypt(self.checking_balance)
    
    def getSavings(self):
        return encrypt_decrypt.decrypt(self.savings_balance)

    def deposit(self, type, amount):
        if type == 'checking':
            self.checking_balance = encrypt_decrypt.decrypt(self.checking_balance)
            self.checking_balance = float(self.checking_balance) + float(amount)
            self.checking_balance = encrypt_decrypt.encrypt(self.checking_balance)

        elif type == 'savings':
            self.savings_balance = encrypt_decrypt.decrypt(self.savings_balance)
            self.savings_balance = float(self.savings_balance) + float(amount)
            self.savings_balance = encrypt_decrypt.encrypt(self.savings_balance)

        else:
            print('Invalid Balance Type')

    def withdraw(self, type, amount):
        if type == 'checking':
            self.checking_balance = encrypt_decrypt.decrypt(self.checking_balance)

            if float(amount) > float(self.checking_balance):
                print('Insufficient Funds in Checking Account')
            else:
                self.checking_balance = self.checking_balance - amount
                print("$" + str(amount) + " withdrawn from checking account")

            self.checking_balance = encrypt_decrypt.encrypt(self.checking_balance)

        elif type == 'savings':
            self.savings_balance = encrypt_decrypt.decrypt(self.savings_balance)

            if float(amount) > float(self.savings_balance):
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

    def printInfor(self):
        User.printInfo(self)
        print("Checking balance: $", encrypt_decrypt.decrypt(self.checking_balance))
        print("Saving balance: $", encrypt_decrypt.decrypt(self.savings_balance))

# TESTING ########################################################################
#user = Account("Sabrina Lugo", "salugo0721", "Sweet1", "20.00")
# user.printInfor()
#print("Name: ", user.getUser())
#print("Username: ", user.getUsername())
#print("Password: ", user.getPassword())
#print("Checking: $", user.getChecking())
#print("Savings: $", user.getSavings())
#Database = [0,0,0]
#for i, v in enumerate(Database):
#    if v == 0:
#        Database[i] = Account("Sabrina Lugo", "salugo0721", "Sweet1", "20.00")  
#user = Database[0]
#del user
#user.printInfor()
#Database[0] = 0
#Database[0].printInfor()
##################################################################################

        


