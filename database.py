import models
from encrypt_decrypt import encrypt, decrypt

#delete, and search need to be created 

Database = [models.Account('void', 'void', 'void', 0, 0) for i in range(10)]

#####################################################################
# hashfunction(): 
# converts username and password to ascii value and returns the value  
#####################################################################

def hashFunction(username, password): #tested  
    key = 0 

    for i in username:
        key = key + ord(i)
    for i in password:
        key = key + ord(i)
        
    return key % len(Database)

####################################################################
# upload():
# uploads data from file.txt
####################################################################
    
def upload(): #tested

    file = open("database.txt",'r')
    line = file.readline()

    while line != '':
        if line != '0':
            name, username, passwd, checking, savings = line.split()

            insert(name, decrypt(username), decrypt(passwd), decrypt(checking), decrypt(savings))

            line = file.readline()

    file.close()

####################################################################
# overwrite():
# overwrites file.txt with the information in the new database
# use after insert(), but not in it (since insert() is used in upload())
####################################################################

def overwrite():

    file = open('database.txt', 'w')

    for account in Database:
        file.write('{} {} {} {} {}\n'.format(account.user, account.username, account.password_hash, account.checking_balance, account.savings_balance))

    file.close()

  #################################################################
  # insert()
  # inserts a user with their information inside 
  # the database
  #################################################################    

def insert(name, username, passwd, checking, savings=0):
        key =  hashFunction(username, passwd)
        j = 1

        for i,v in enumerate(Database):
            while(key == i and v.getUsername() != 'void'):
                 key = (key + j) % len(Database)
                 j = j + 1
                 
            if(key == i and v.getUsername() == 'void'):
                Database[key] = models.Account(name, username, passwd, checking, savings)

####################################################################
# delete()
# deletes user object and frees space in Database.
####################################################################
def delete(user,key): #tested

    del Database[key]
    Database[key] = models.Account('void', 'void', 'void', 0, 0)

    overwrite()

####################################################################
#
#
####################################################################

# I was getting an error with this search function because it said b was an int instead of an Account object
# def search(username, key):
#     for k,b in enumerate(Database):
#         if key == k:
#             if username == b.getUsername():
#                 return k
#             else:
#                 for k,b in enumerate(Database):             # -> while(k < len(Database))
#                     if(username == b.getUsername()):        # -> Database[k].getUsername()
#                         return k
#                     elif(k == len(Database) - 1) and username != b.getUsername():
#                         k = 0

def search(username, key):
    k = key
    while username != Database[key].getUsername():
        key = (key + 1) % len(Database)
        if key == k:
            # user not found
            return -1
    return key
            



###################################################################
# menu()
# outputs a menu for the user to chose from 
# option is return 
################################################################### 
            
def menu():

    print(" MENU ")
    print("------")
    print("1. Login")
    print("2. Sign up")
    print("3. Quit")

    option = input("Enter an option(NUMBER ONLY): ")

    return option
###################################################################
# transactions()
# displays a list of transactions the user can 
# do 
# option is return 
###################################################################

def transactions():
    print(" TRANSACTIONS ")
    print("--------------")
    print("1. Deposit. ")
    print("2. Withdraw")
    print("3. Delete account")
    print("4. View balance")
    print("5. Quit")

    option = input("Enter an option: ")

    return option

####################################################################
# main()
# beginning of the program
####################################################################

def main():

    upload()
    print(len(Database))

    option = menu()
    option = int(option)

    while(option < 3):
        if (option == 1):
            found = False
            while(found == False):
                username = input("Username: ")
                password = input("Password: ")

                key = hashFunction(username, password)
                if search(username, key) != -1:
                    user = Database[search(username, key)]
                    found = True
                else:
                    print('Invalid Username or Password')                           

            option = transactions()
            option = int(option)

            while(option < 5):
                if(option == 1):

                    valid_type = False
                    while(valid_type == False):
                        a_type = input("Deposit to checking or savings? ")
                        deposit = input("Enter amount to deposit: ")

                        if(a_type == 'checking'):
                            valid_type = True
                        if(a_type == 'savings'):
                            valid_type = True

                        user.deposit(a_type, deposit)
                        

                elif(option == 2):

                    valid_type = False
                    while(valid_type == False):
                        a_type = input("Withdraw from checking or savings? ")
                        withdraw = input("Enter amount to withdraw: ")

                        if(a_type == 'checking'):
                            valid_type = True
                        if(a_type == 'savings'):
                            valid_type = True

                        user.withdraw(a_type, withdraw)

                elif(option == 3):

                    delete(user, key) 

                else:

                    valid_type = False
                    while(valid_type == False):

                        a_type = input("View checking or savings? ")

                        if(a_type == 'checking'):
                            valid_type = True
                        if(a_type == 'savings'):
                            valid_type = True

                        user.view_balance(a_type)

                option = transactions()
                option = int(option)
            
        

        elif(option == 2):

            username = input("Enter a username: ")
            password = input("Enter a password: ")

            key = hashFunction(username, password)

            user = Database[search(username, key)]

            while (username == user.getUsername()):

                print("Username is not available.")
                username = input("Enter another username: ")

                key = hashFunction(username, password)

                user = Database[search(username, key)]

            name = input("Enter your name: ")
            checking = input("Deposit: ")

            insert(name, username, password, checking)
            overwrite()

            print("Your account has been created. ")

        option = menu()
        option = int(option)





                    

                

            








