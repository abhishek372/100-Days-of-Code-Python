# Banker Roulette - who's paying

import random

names = input().split(", ")

# name = random.choices(names_string)
# print(name[0])

# we can also do this way
x = len(names)

random_choice = random.randint(0, x-1)
person_going_to_pay = names[random_choice]

print(person_going_to_pay + " is going to buy the meal today.")
