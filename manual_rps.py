import random

def get_computer_choice (): # This function randomly picks an option from "rock, paper, scissors" and returns it as the computer's choice.
    possible_choices = ["rock", "paper", "scissors"]
    computer_chose = random.choice(possible_choices)
    return computer_chose

def get_user_choice(): # This function allows the user to choose an option from "rock, paper, scissors" and returns it as the user's choice.
    user_chose = input("Enter a choice (rock, paper, scissors): ")
    print(f"You chose {user_chose}.")
    return user_chose

def get_winner(user_choice, computer_choice): # This function gets the winner of the game.

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

def play():
    comp_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(user_choice, comp_choice)
    return

play()