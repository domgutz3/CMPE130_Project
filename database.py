import models

#delete, and search need to be created 

Database = [0 for i in range(10)]

#####################################################################
# hashfunction(): 
# converts username and password to ascii value and returns the value  
#####################################################################

def hashFunction(username, password):   
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
    
def upload():

    file = open("database.txt",'r')
    line = file.readline()

    while line != '':
        name, username, passwd, checking = line.split()

        insert(name, username, passwd, checking)

        line = file.readline()

    file.close()

  #################################################################
  # insert()
  # inserts a user with their information inside 
  # the database
  #################################################################    

def insert(name, username, passwd, checking):
        key =  hashFunction(username, passwd)

        j = 1
        for i,v in enumerate(Database):
            while(key == i and v != 0):
                 key = (num + j) % len(Database)
                 j = j + 1
                 
            if(key == i and v == 0):
                Database[key] = models.Account(name, username, passwd, checking, 0)

####################################################################
# delete()
#
####################################################################
def delete():

####################################################################
#
#
####################################################################

def search():

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
            user = search(key)                          #not sure about this 

            option = transactions()

            while(option < 5):
                if(option == 1):
                    deposit = input("Enter amount to deposit: ")
                    user.models.deposit(deposit)

                elif(option == 2):
                    withdraw = input("Enter amount to withdraw: ")
                    user.models.withdraw(withdraw)
                elif(option == 3):
                    delete(user) 
                else:
                    user.models.view_balance()

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
            print("Your account has been created. ")

        menu()





                    

                

            








