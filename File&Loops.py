try:
    store = {}
    Assignment = open('assignment.txt', 'w')
    for x in range(5):
        user = input('Write your full name here:')
        Assignment.write('Username: '+ user +'\n')
        store['Name'] = user
        password = input('Type in your pin:')
        Assignment.write('Password: '+ password + '\n')
        store['Pin'] = password
        Assignment.write("person = "+str(store)+'\n')
        print('Successful')
    Assignment.close()
    print('Database Full')
except Exception as Error:
    print(Error)