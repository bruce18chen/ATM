"""
Ask user for their PIN number. The useer has 3 attempts to enter\
the correct pin until they are locked out of their account.
"""

input_pin = input('Please enter your PIN:')
COUNTER = 1

while COUNTER <= 3:
    if input_pin =='1234':
        print('Your account balance is : 0. Goodbye!')
        exit()
    elif COUNTER == 3:
        print('Account locked. The police is on the way.')
        exit()
    else:
        COUNTER +=1
        print('Invalid pin')
        input_pin = input('Please enter your PIN:')
