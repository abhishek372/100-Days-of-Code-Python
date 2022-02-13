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

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

choice = int(choice)
elements = [rock, paper, scissors]

computer_chosen = random.randint(0, len(elements)-1)

# print(choice, computer_chosen)

if (choice==0) and (computer_chosen==0):
    print(rock)
    print("\nComputer chose:\n")
    print(rock)
    print("Match drawn")
elif (choice == 0) and (computer_chosen == 1):
    print(elements[0])
    print("\nComputer chose:\n")
    print(elements[1])
    print("Computer wins")
elif (choice == 0) and (computer_chosen == 2):
    print(elements[0])
    print("\nComputer chose:\n")
    print(elements[2])
    print("You win")
elif (choice == 1) and (computer_chosen == 0):
    print(elements[1])
    print("\nComputer chose:\n")
    print(elements[0])
    print("You wins")
elif (choice == 1) and (computer_chosen == 1):
    print(elements[1])
    print("\nComputer chose:\n")
    print(elements[1])
    print("Match drawn")
elif (choice == 1) and (computer_chosen == 2):
    print(elements[1])
    print("\nComputer chose:\n")
    print(elements[2])
    print("Computer wins")
elif (choice == 2) and (computer_chosen == 0):
    print(elements[2])
    print("\nComputer chose:\n")
    print(elements[0])
    print("Computer wins")
elif (choice == 2) and (computer_chosen == 1):
    print(elements[2])
    print("\nComputer chose:\n")
    print(elements[1])
    print("You wins")
elif (choice == 2) and (computer_chosen == 2):
    print(elements[2])
    print("\nComputer chose:\n")
    print(elements[2])
    print("Match drawn")



