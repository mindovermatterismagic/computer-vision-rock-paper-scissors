import random 
import cv2
from keras.models import load_model
import numpy as np
import time

class computer_vision_rps:

    # Returns a random choice from the rps list for the computer_choice
    def get_computer_choice(self):
        rps  = ['Rock', 'Paper', 'Scissors']
        return random.choice(rps)

    # Returns the prediction from the model using the input from the webcam
    # as either Rock, Paper or Scissors
    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Uses the time() method to save the start time
        start_time = time.time()
        # Runs the while loop for three seconds 
        while (time.time() - start_time) < 3:

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Defines a list with the deep learning models labels
            # this is used to match the highest probability with its corresponding label.
            rps = ["Rock", "Paper", "Scissors", "Nothing"]
            # Saves the prediction by finding the index of the highest probability
            # and then indexes the rps list with the same index.
            rps_prediction = rps[prediction[0].tolist().index(max(prediction[0]))]
        # After the loop release the cap objects
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        # Validates the prediction to ensure it isn't "Nothing" which wouldn't work
        # with the rest of the program. 
        if rps_prediction == "Nothing":
            print("You haven't picked an option please gesture Rock, Paper or Scissors")
            # If the prediction is "Nothing" the method is called again so the user
            # can make another input.
            self.get_prediction(self)
        else:
            print(f"You have chosen {rps_prediction}!")
            return rps_prediction

    # Compares the computer_choice and the user_choice to determine the winner.
    # Prints the computers choice and then a message to say if the user won, lost or it was a tie.
    # Returns the winner
    def get_winner(self, computer_choice, user_choice):
        winner = ''
        if computer_choice == user_choice:
            print(f"The computer chose {computer_choice}!")
            print('It is a tie!')
            winner = 'Tie'
        elif computer_choice == 'Rock':
            print(f"The computer chose {computer_choice}!")
            if user_choice == 'Paper':
                print('You won!')
                winner = 'User'
            else:
                print('You lost')
                winner = 'Computer'
        elif computer_choice == 'Paper':
            print(f"The computer chose {computer_choice}!")
            if user_choice == 'Scissors':
                print('You won!')
                winner = 'User'
            else:
                print('You lost')
                winner = 'Computer'
        elif computer_choice == 'Scissors':
            print(f"The computer chose {computer_choice}!")
            if user_choice == 'Rock':
                print('You won!')
                winner = 'User'
            else:
                print('You lost')
                winner = 'Computer'
        return winner

# Instantiates a computer_vision_rps object and then plays the game.
def play():

    # creates object
    game = computer_vision_rps()

    # Keeps track of the wins for each player as well as the number of rounds played.
    computer_wins = 0
    user_wins =  0
    rounds_played = 0

    #Rounds are played until either player reaches 3 wins or 5 rounds have been played.
    while computer_wins < 3 and user_wins < 3 and rounds_played < 5:
        computer_choice = game.get_computer_choice()
        user_choice = game.get_prediction()
        winner = game.get_winner(computer_choice, user_choice)
        if winner == "Computer":
            computer_wins += 1
        elif winner == "User":
            user_wins += 1
        print(f"The computer has {computer_wins} wins!")
        print(f"You have {user_wins} wins!")
        rounds_played += 1
    
    if computer_wins == 3:
        print("Sorry. You Lost")
    elif user_wins == 3:
        print("You won the game! Hurray!")
    else:
        print("It is a draw, nobody reached 3 wins within 5 rounds")

play()
