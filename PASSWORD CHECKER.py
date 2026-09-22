#This is a program to check whether a password is a strong or a moderate or a weak password.
def password_checker():
    while True:
        password = input('Enter your password: ')

        caps_char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        small_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        num = [0,1,2,3,4,5,6,7,8,9]
        sp_char = ['.','_','@',' ',',','&']

        if caps_char in password and small_char in password and num in password and sp_char in password:
            print('Your password is a strong one!')
        elif caps_char and small_char and num in password:
            print('Your password is a moderate one!')
        else:
            print('It is a weak password!')
    
        continuation = input('Do you want to continue? (y/n): ').lower()
        if continuation == 'n':
            print('Thank You for using my password checker!')
            break
        elif continuation == 'y':
            continue
        else:
            print('Error occured!')
password_checker()