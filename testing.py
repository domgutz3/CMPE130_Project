import models
import database

Database = [models.Account('void', 'void', 'void', 0, 0) for i in range(10)]

# def insert(name, username, passwd, checking, savings=0): 
#         key =  database.hashFunction(username, passwd)

#         i = 0
#         j = 1

#         while (i < len(Database)):

#             if(key == i and Database[i] == 0):
#                 Database[key] = models.Account(name, username, passwd, checking, savings)
#             else:
#                 while (Database[i] != 0):
#                     key = (key + j) % len(Database)
#                     j = j + 1
#                 Database[key] = models.Account(name, username, passwd, checking, savings)

def hashFunction(username, password): #tested  
    key = 0 

    for i in username:
        key = key + ord(i)
    for i in password:
        key = key + ord(i)
        
    return key % len(Database)

                
def insert(name, username, passwd, checking, savings=0):
        key =  hashFunction(username, passwd)
        j = 1

        for i,v in enumerate(Database):
            while(key == i and v.getUsername() != 'void'):
                 key = (key + j) % len(Database)
                 j = j + 1
                 
            if(key == i and v.getUsername() == 'void'):
                Database[key] = models.Account(name, username, passwd, checking, savings)
 

def delete(position):
    
    del Database[position]
    Database[position] = 0

def main():
    upload()
    # Database[0] = models.Account('Sabrina Lugo', 'salugo721','Sweet1', '100.00')
    # Database[1] = models.Account('Dominic Gutierrez', 'dom123', 'Liljoker3','350.00')
    # Database[2] = models.Account('Kenneth Lu', 'ken454','2coo4u', '230.0')

    #position = int(input("Enter a position: "))

    insert('Ron Lencevicus', 'RonL546', 'Babycakes1', '324.0')
    insert('Sabrina Lugo', 'salugo721','Sweet1', '100.00')
    insert('Dominic Gutierrez', 'dom123', 'Liljoker3','350.00')

    print('\n')

    for i in Database:
        i.printInfor()
        print('\n')

    #Database[position].printInfor()
    #print('\n')
    #delete(position)
    #Database[position].printInfor()
    #print(Database[position])

string = "This is a string."

for line in file: 
    list(line.split())






