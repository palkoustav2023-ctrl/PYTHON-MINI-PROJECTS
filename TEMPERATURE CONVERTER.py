#This is a program to convert temperature (Degree Celcius and Degree Fahrenheit)
def temperature_converter():
    while True:
        print('Welcome to temperature converter!')
        temp = float(input('Enter the temperature (Degree Centigrade or Degree Fahrenheit): '))
        conv = input('In which unit you want to convert? (Degree centigrade or Degree fahrenheit): ').lower()
        if conv == 'degree centigrade' or conv == 'degree celcius' or conv == 'celcius' or conv == 'centigrade':
            cen = ((temp - 32)*5)/9
            print(f'Your temperature in Degree Centigrade is {cen}')
        elif conv == 'degree fahrenheit' or conv == 'fahrenheit':
            fah = ((temp*9)+160)/5
            print(f'Your temperature in Degree Fahrenheit is {fah}')
        else:
            print('Error occured!')
        continuation = input('Do you want to continue? (y/n): ').lower()
        if continuation == 'n':
            print(f'Thank you for using the converter!')
            break
        elif continuation == 'y':
            continue
        else:
            print('Error occured!')
temperature_converter()