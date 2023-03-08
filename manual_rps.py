import random 

def get_computer_choice():
    rps  = ['Rock', 'Paper', 'Scissors']
    return random.choice(rps)

def get_user_choice():
    user_choice = input('Please enter rock, paper or scissors')
    return user_choice.capitalize()

def get_winner(computer_choice, user_choice):
    winner = ''
    if computer_choice == user_choice:
        print('It is a tie!')
        winner = 'Tie'
    elif computer_choice == 'Rock':
        if user_choice == 'Paper':
            print('You won!')
            winner = 'User'
        else:
            print('You lost')
            winner = 'Computer'
    elif computer_choice == 'Paper':
        if user_choice == 'Scissors':
            print('You won!')
            winner = 'User'
        else:
            print('You lost')
            winner = 'Computer'
    elif computer_choice == 'Scissors':
        if user_choice == 'Rock':
            print('You won!')
            winner = 'User'
        else:
            print('You lost')
            winner = 'Computer'
    return winner

def play():

    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    get_winner(computer_choice, user_choice)


play()