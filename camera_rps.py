import random 
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    rps  = ['Rock', 'Paper', 'Scissors']
    return random.choice(rps)

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    start_time = time.time()
    while (time.time() - start_time) < 3:

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)

        rps = ["Rock", "Paper", "Scissors", "Nothing"]
        rps_prediction = rps[prediction[0].tolist().index(max(prediction[0]))]

    # After the loop release the cap objects
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    if rps_prediction == "Nothing":
        print("You haven't picked an option please gesture Rock, Paper or Scissors")
        get_prediction()
    else:
        print(f"You have chosen {rps_prediction}!")
        return rps_prediction

def get_winner(computer_choice, user_choice):
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

def play():

    computer_choice = get_computer_choice()
    user_choice = get_prediction()

    get_winner(computer_choice, user_choice)

play()
