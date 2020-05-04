import models

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
    return key

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
  ################################################
  # insert()
  # inserts a user with their information inside 
  # the database
  ################################################    

def insert(name, username, passwd, checking):

        num =  hashFunction(username, passwd)
        key = num % len(Database)

        j = 1
        for i,v in enumerate(Database):
            while(key == i and v != 0):
                 key = (num + j) % len(Database)
                 j = j + 1
                 
            if(key == i and v == 0):
                Database[key] = models.Account(name, username, passwd, checking, 0)

upload()





