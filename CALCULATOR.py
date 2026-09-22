#This is a program of a working simple calculator.
def calculator():
    while True:
        n1 = int(input('Enter the first number: '))
        n2 = int(input('Enter the second number: '))

        add = n1+n2
        sub = n1-n2
        mul = n1*n2
        div = n1/n2

        user = input('Enter your required expression(Add/Sub/Mul/Div): ').lower()

        if user == 'add':
            print(f'Your required sum is: {add}')
        elif user == 'sub':
            print(f'Your required difference is: {sub}')
        elif user == 'mul':
            print(f'Your required product is: {mul}')
        elif user == 'div':
            print(f'Your required quotient is: {div}')
        else:
            print('Error occured!')

        continuation = input('Do you want to continue?(y/n): ').lower()
        if continuation == 'y':
            continue
        elif continuation == 'n':
            print(f'Thank You for using my simple calculator!')
            break
        else:
            print(f'Error occured!')
calculator()