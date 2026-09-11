#This is a program of a working ATM system in Python.

#This part is for the user to make their own pin, username and balance according to their needs.
username = 'palkoustav2023'
pin = 251200
balance = 1000

print('Welcome to the ATM system!')

#This is the part where user will enter their username and pin to access the ATM system.
user_name = input('Please enter your username: ')
user_pin = int(input('Please enter your pin: '))

#This is the part where the program checks what condition is met.
if username == user_name and pin == user_pin:
    print('Access Granted! Welcome!')
    while True:
        user = input('What do you want to do (Withdraw, Deposit, Balance, Exit)?: ').lower()
        if user == 'withdraw':
            withdraw = int(input('Enter amount to be withdrawn: '))
            if balance >= withdraw:
                balance -= withdraw
                print(f'''Amount withdrawn successfully!
                Your current account balance is: {balance}''')
            else:
                print(f'''Insufficient account balance!
                Balance: {balance}''')
        elif user == 'deposit':
            deposit = int(input('Enter amount to be deposited: '))
            balance += deposit
            print(f'''Amount deposited successfully!
            Your current account balance is: {balance}''')
        elif user == 'balance':
            print(f'Your current account balance is: {balance}')
        elif user == 'exit':
            print('Thank You for using our ATM! Please come back again!')
            break
        else:
            print('Error occured! Please recheck!')
else:
    print('Sorry! Access Denied!')