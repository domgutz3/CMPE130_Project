import models

'''
Read in Database File
'''
file = open('database.txt', 'r')
lines = []
lines = file.readlines()
lines = [line.strip() for line in lines]
lines = [line.split() for line in lines]
Database = []
i = 0
for line in lines:
    Database.append(models.Account(line[0], line[1]))
for i in range(len(Database)):
    Database[i].deposit('checking', int(lines[i][2]))
    Database[i].deposit('savings', int(lines[i][3]))
'''
Database Created
'''


Database[0].deposit('checking', 400)

print(Database[0].view_balance('checking'))







'''
Writing to Database File
'''
file.close()
file = open('database.txt', 'w')

for x in Database:
    file.write('{} {} {} {}\n'.format(x.username, x.password_hash, x.checking_balance, x.savings_balance))
'''
Database File Updated
'''
file.close()