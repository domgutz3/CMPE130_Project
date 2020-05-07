import models
import database

Database = [0 for i in range(3)]

def delete(position):
    
    del Database[position]
    Database[position] = 0

def main():

    Database[0] = models.Account('Sabrina Lugo', 'salugo721','Sweet1', '100.00')
    Database[1] = models.Account('Dominic Gutierrez', 'dom123', 'Liljoker3','350.00')
    Database[2] = models.Account('Kenneth Lu', 'ken454','2coo4u', '230.0')

    position = int(input("Enter a position: "))

    Database[position].printInfor()
    print('\n')
    delete(position)
    #Database[position].printInfor()
    print(Database[position])

main()



