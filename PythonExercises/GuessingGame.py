'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
'''

import random



num_of_guesses = int(0)
num = random.randint(1,9)

while True:
    
    guess = int(input("Please enter a number between 1 - 9 "))
    
    if(guess < num):
        print("Your number is too low")
        num_of_guesses += 1
        continue
    elif (guess > num):
        print("Your guess is too high")
        num_of_guesses += 1
        continue
    else:
        print("You guessed it right")
        print(f"Number of Guesses: {num_of_guesses}")
        play_again = input("type 'exit' to exit the program or hit enter to continue")
        if(play_again == "exit"):
            break
        else:
            num_of_guesses = 0
            num = random.randint(1,9)
            continue
        
        