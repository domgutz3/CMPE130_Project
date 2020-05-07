import models

#delete, and search need to be created 

Database = [0 for i in range(10)]

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
        name, username, passwd, checking, savings = line.split()

        insert(name, username, passwd, checking, savings)

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
        file.write('{} {} {} {} {}\n'.format(account.name, account.username, account.password_hash, account.checking_balance, account.savings_balance))

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
            while(key == i and v != 0):
                 key = (key + j) % len(Database)
                 j = j + 1
                 
            if(key == i and v == 0):
                Database[key] = models.Account(name, username, passwd, checking, savings)

####################################################################
# delete()
# deletes user object and frees space in Database.
####################################################################
def delete(user,key): #tested

    del Database[key]
    Database[key] = 0

    overwrite()

####################################################################
#
#
####################################################################

def search(username, key):

    for k,b in enumerate(Database): 
        if key == k:
            if username == b.getUsername():
                return k
            else:
                for k,b in enumerate(Database):        # -> while(k < len(Database)):
                    if(username == b.getUsername()):   # -> Database[k].getUsername() 
                        return k
                    elif(k == len(Database) - 1) and username != b.getUsername():
                        k = 0
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

    option = menu() 
    while(option < 3):
        if (option == 1):

            username = input("Username: ")
            password = input("Password: ")

            key = hashFunction(username, password)
            user = search(username, key)                           

            option = transactions()

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
            
        

        elif(option == 2):

            username = input("Enter a username: ")
            password = input("Enter a password: ")

            key = hashFunction(username, password)

            user = search(key)

            while (username == user.getUsername()):

                print("Username is not available.")
                username = input("Enter another username: ")

                key = hashFunction(username, password)

                user = search(key)

            name = input("Enter your name: ")
            checking = input("Deposit: ")

            insert(name, username, password, checking)
            overwrite()

            print("Your account has been created. ")

        menu()





                    

                

            








