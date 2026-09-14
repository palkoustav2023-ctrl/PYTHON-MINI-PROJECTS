#This is a program to play the game of Rock, Paper, Scissors in Python.
def rock_paper_scissors():
    import random as r

    while True:
        choices = r.choice(['rock','paper','scissors'])
        user = input('Enter your choice (rock, paper, scissors): ').lower()
        if user == choices:
            print(f'It is a tie! both chose {user}')
        elif user == 'rock' and choices == 'paper':
            print(f'You lose! {choices} beats {user}')
        elif user == 'rock' and choices == 'scissors':
            print(f'You won! {user} beats {choices}')
        elif user == 'paper' and choices == 'rock':
            print(f'You won! {user} beats {choices}')
        elif user == 'paper' and choices == 'scissors':
            print(f'You lose! {choices} beats {user}')
        elif user == 'scissors' and choices == 'rock':
            print(f'You lose! {choices} beats {user}')
        elif user == 'scissors' and choices == 'paper':
            print(f'You won! {user} beats {choices}')
        else:
            print('Error occured! Please recheck!')

        continuation = input('DO you want to continue (y/n)?: ')
        if continuation == 'n':
            print('Thank You for playing Rock, Paper, Scissors with me!')
            break

rock_paper_scissors()