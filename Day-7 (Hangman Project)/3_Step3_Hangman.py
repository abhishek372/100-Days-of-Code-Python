# Step 3

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f"The chosen_word is {chosen_word}")

display = []

for _ in range(len(chosen_word)):
    display.append("_")
print(display)

# Todo-1 - Using while loop which let the user to guess again. The loop should only stop
# once the user guessed all the letters in the chosen_word and display has no more blanks("_").
# Then, we can say that user won.

i = 0
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        print(f"Current position : {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = guess

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")


