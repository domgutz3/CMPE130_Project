import models
from encrypt_decrypt import encrypt, decrypt
from random import randrange

Database = [models.Account('void','void', 'void', 'void', 0, 0) for i in range(10)]

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
        #if line != '0':
        first, last, username, passwd, checking, savings = line.split()

        insert(first, last, username, passwd, checking, savings)

        line = file.readline()

    file.close()

####################################################################
# overwrite():
# overwrites file.txt with the information in the new database
# use after insert(), but not in it (since insert() is used in upload())
####################################################################

def overwrite():

    file = open("output.txt", 'w')

    for account in Database:
        file.write('{} {} {} {} {}\n'.format(account.user, decrypt(account.username), 
        decrypt(account.password_hash), decrypt(account.checking_balance), decrypt(account.savings_balance)))

    file.close()

#################################################################
# insert()
# inserts a user with their information inside 
# the database
#################################################################    

def insert(first, last, username, passwd, checking, savings=0):
        key =  hashFunction(username, passwd)
        j = 1

        for i,v in enumerate(Database):
            while(key == i and v.getUsername() != 'void'):
                 key = (key + j) % len(Database)
                 j = j + 1
                 
            if(key == i and v.getUsername() == 'void'):
                Database[key] = models.Account(first, last, username, passwd, checking, savings)

####################################################################
# delete()
# deletes user object and frees space in Database.
####################################################################
def delete(username,key): #tested
    Database[search(username, key)] = models.Account('void', 'void', 'void', 'void', 0, 0)
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
# sort()
# outputs a list of all accounts, sorted by largest total balance
# used by bank owner to determine most valuable accounts
################################################################### 

def sort(A):
    list = A
    randomQuickSort(list, 0, len(list) - 1)
    for item in list:
        print(item.getUser() + ', Balance: ' + str(item.getTotalBalance()))

def randomQuickSort(A, p, r):
    if p < r:
        q = randomPartition(A, p, r)
        randomQuickSort(A, p, q)
        randomQuickSort(A, q + 1, r)

def partition(A, p, r):
    x = A[p].getTotalBalance()
    i = p - 1
    j = r + 1
    while(True):
        j = j - 1
        while A[j].getTotalBalance() > x:
            j = j - 1
        i = i + 1
        while A[i].getTotalBalance() < x:
            i = i + 1
        if i < j:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
        else:
            return j

def randomPartition(A, p, r):
    i = randrange(p, r)
    temp = A[i]
    A[i] = A[p]
    A[p] = temp
    return partition(A, p, r)




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
    print("3. List Accounts")
    print("4. Quit")
    print('\n')

    option = input("Enter an option(NUMBER ONLY): ")
    print('\n')

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
    print("\n")

    option = input("Enter an option: ")

    print("\n")

    return option

####################################################################
# main()
# beginning of the program
####################################################################

def main():
    upload()

    option = int(menu())

    while(option < 4):
        if (option == 1):
           
            username = input("Username: ")
            password = input("Password: ")

            key = hashFunction(username, password)
            if search(username, key) != -1:
                user = Database[search(username, key)]

                option = int(transactions())

                while(option < 5):
                    if(option == 1):

                        valid_type = False
                        while(valid_type == False):
                            a_type = input("Deposit to checking or savings? ")
                            deposit = float(input("Enter amount to deposit: "))

                            if(a_type == 'checking'):
                                valid_type = True
                            if(a_type == 'savings'):
                                valid_type = True

                        user.deposit(a_type, deposit)
                        overwrite()
                        

                    elif(option == 2):

                        valid_type = False
                        while(valid_type == False):
                            a_type = input("Withdraw from checking or savings? ")
                            withdraw = float(input("Enter amount to withdraw: "))

                            if(a_type == 'checking'):
                                valid_type = True
                            if(a_type == 'savings'):
                                valid_type = True

                        user.withdraw(a_type, withdraw)
                        overwrite()

                    elif(option == 3):

                        delete(username, key)
                        break

                    else:

                        valid_type = False
                        while(valid_type == False):

                            a_type = input("View checking or savings? ")

                            if(a_type == 'checking'):
                                valid_type = True
                            if(a_type == 'savings'):
                                valid_type = True

                            user.view_balance(a_type)
                    option = int(transactions())
            else:
                print('Invalid Username or Password')

            

                      
                
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

            first = input("Enter your first name: ")
            last = input("Enter your last name: ")

            checking = input("Deposit: ")

            insert(first, last, username, password, checking)
            overwrite()

            print("Your account has been created. ")                        

            
            #option = int(option)  

        elif(option == 3):
            sort(Database)

        option = int(menu())
        #option = int(option)
main()





                    

                

            








