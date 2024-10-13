username_storage = 'angel'
password_storage = 'angel1000'


print('Login to the system \n')

attempt_counter = 0

while attempt_counter < 4:

    username = input('Enter Username: ')
    password = input('Enter password: ')

    if username == username_storage and password == password_storage:
        print('Username or Password is correct')
        attempt_counter +=1
        break
    else:
        print('Username or Password is incorrect. Try Again')
        attempt_counter +=1

if attempt_counter > 3:
    print('You are out of attempts, please try later')