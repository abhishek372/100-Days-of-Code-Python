# Step 2

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f"The chosen_word is {chosen_word}")

# Todo-1 - Create an empty list called display. For each letter in chosen_word, add "_" to 'display'.
display = []

for _ in range(len(chosen_word)):
    display.append("_")
print(display)

guess = input("Guess a letter: ").lower()

# Todo-2 - Loop through each position in the chosen_word. If the letter at that position matches 'guess' reveal that letter in display.
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess

# Todo-3 - Print the display
print(display)