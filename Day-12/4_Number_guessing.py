# Number Guessing game


# Importing modules
import random
from art import logo

# Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to set the difficulty
def set_difficulty():
    """Ask the user to set the difficulty. And, returns the level of game."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level=='hard':
        return HARD_LEVEL_TURNS


# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """Checks the guess number against answer. Returns the number of turns"""
    if guess > answer:
        print("Too high.")
        return turns - 1 
    elif guess < answer:
        print("Too low.")
        return turns - 1 
    else:
        print(f"You got it! The answer was {guess}.")


# Function to start the game
def game():
    # Prints logo
    print(logo)
    print("Welcome to Number Guessing Game!")

    # Choosing a random number between 1 and 100
    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Psst, the answer is {answer}.")

    # Get the number of turns
    turns = set_difficulty()
    
    guess = 0

    # Repeat the guessing functionality if they get it wrong.
    while guess!= answer:
        print(f"You have {turns} attempts remaining to guess a number.")

        # Let the user guess a number
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce it by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
    
        if turns == 0:
            print(f"You run out of guesses. You lose!")
            return
        elif guess!= answer:
            print("Guess again.")


# Call the game function
game()  