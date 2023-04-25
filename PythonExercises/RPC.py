
'''
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
'''

import random

while True:
    
    user_input = input("rock, paper or scissors: ")
    computer_input = random.choice(['rock', 'paper', 'scissors'])
    
    print("You chose:", user_input)
    print("Computer chose:", computer_input)
    
    if (user_input == computer_input):
        print("Tie!")
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        print("You win!")
    elif(user_input != "rock" or user_input != "paper" or user_input != "scissors"):
        print("Invalid Input")
    else:
        print("You lose!")
    
    play_again = input("Do you want to play again? (y/n): ")
    
    if play_again != 'y':
        break
  
