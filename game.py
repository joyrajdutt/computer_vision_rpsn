# The Necessary Imports

import random
import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class CVRPS:

    def __init__(self, list_choices): #initializing the attributes
        self.list_choices = list_choices
        self.computer_wins = 0
        self.user_wins = 0
        self.end = False

    def get_computer_choice(self, list_choices): # This function randomly picks an option from "rock, paper, scissors" and returns it as the computer's choice.
        return random.choice(list_choices)

    def get_prediction(self): 
        
        start_time = time.time()
        end_time = start_time + 5
        countdown = start_time + 4
        cap = cv2.VideoCapture(0)
        
        while time.time() < end_time: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalizing the image
            data[0] = normalized_image
            prediction = model.predict(data)
            print(prediction)
            
            while time.time() < countdown: # Initiating Countdown Timer
                message = f'Show in... {int(end_time - time.time())}'
                break
            
            while countdown < time.time() < end_time:
                message = 'Show your hand!'
                break

                    # Press q to close the window
            cv2.putText(frame, message, (30, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        if prediction[0][0] > 0.5:
            return "Rock"
        elif prediction[0][1] > 0.5:
            return "Paper"
        elif prediction[0][2] > 0.5:
            return "Scissors"
        else:
            return "Nothing"


    def get_winner(self, user_choice, computer_choice):
        
        if user_choice == 'Rock' and computer_choice == 'Scissors':
            self.user_wins += 1
            return 'You win!'

        elif user_choice == 'Rock' and computer_choice == 'Paper':
            self.computer_wins += 1
            return 'You lose.'
        
        elif user_choice == 'Scissors' and computer_choice == 'Paper':
            self.user_wins += 1
            return 'You win!'
        
        elif user_choice == 'Scissors' and computer_choice == 'Rock':
            self.computer_wins += 1
            return 'You lose.'

        elif user_choice == 'Paper' and computer_choice == 'Rock':
            self.user_wins += 1
            return 'You win!'
        
        elif user_choice == 'Paper' and computer_choice == 'Scissors':
            self.computer_wins += 1
            return 'You lose.'
            
        elif user_choice == computer_choice:
            return 'It\'s a draw!'
        
        else:
            return 'error'

    def play(self):

        while not self.end:
            computer_choice = self.get_computer_choice(list_choices)
            user_choice = self.get_prediction()
            get_winner = self.get_winner(user_choice, computer_choice)
            print(f'\nComputer chose {computer_choice}.')
            if self.computer_wins == 3:
                print('Game Over!\nComputer Wins!')
                self.end = True
            elif self.user_wins == 3:
                print('Game Over!\nYou Win!')
                self.end = True
            else:
                print(f'\n{get_winner}')
        
list_choices=['Rock', 'Paper', 'Scissors']
p = CVRPS(list_choices)
p.play()