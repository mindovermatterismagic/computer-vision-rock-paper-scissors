import random 

def get_computer_choice():
    rps  = ["rock", "paper", "scissors"]
    return random.choice(rps)

def get_user_choice():
    user_choice = input("Please enter rock, paper or scissors")
    return user_choice.lower()

computer_choice = get_computer_choice()
user_choice = get_user_choice()

def get_winner(computer_choice, user_choice):
    winner = ""
    if computer_choice == user_choice:
        print("It's a tie")
        winner = "Tie"
    elif computer_choice == "rock":
        if user_choice == "paper":
            print("You won")
            winner = "User"
        else:
            print("You lost")
            winner = "Computer"
    elif computer_choice == "paper":
        if user_choice == "scissors":
            print("You won")
            winner = "User"
        else:
            print("Computer Wins")
            winner = "You lost"
    elif computer_choice == "scissors":
        if user_choice == "rock":
            print("You won")
            winner = "User"
        else:
            print("You lost")
            winner = "Computer"
    return winner

get_winner(computer_choice, user_choice)