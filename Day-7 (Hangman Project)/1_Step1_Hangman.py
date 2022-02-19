# Step 1

import random

word_list = ["ardvark", "baboon", "camel"]

# Todo-1 - Randomly choosen word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# Testing code
print(f"The chosen_word is {chosen_word}")

# Todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# Todo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if guess == letter:
        print("Right guess")
    else:
        print("Wrong guess")