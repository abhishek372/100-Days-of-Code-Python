# Rock Paper Scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

game_elements = [rock, paper, scissors]

computer_chosen = random.randint(0, len(game_elements)-1)

print(game_elements[choice])
print("Computer chose: \n" ,game_elements[computer_chosen])

if (choice == computer_chosen):
    print("Match drawn")
elif (choice == 0) and (computer_chosen == 1):
    print("You lose!")
elif (choice == 0) and (computer_chosen == 2):
    print("You win")
elif (choice == 1) and (computer_chosen == 0):
    print("You win")
elif (choice == 1) and (computer_chosen == 2):
    print("You lose!")
elif (choice == 2) and (computer_chosen == 0):
    print("You lose!")
elif (choice == 2) and (computer_chosen == 1):
    print("You win")



