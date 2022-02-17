# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '^', '&', '*', '(', ')','+']


# Greeting message
print("Welcome to the PyPassword Generator")

# Inputs from user
nr_letters = int(input("How many letters would you like to have in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Easy level
# trty%#892

password = ""

# Random letters
for i in range(nr_letters):
    password += random.choice(letters)

# Random numbers
for i in range(nr_numbers):
    password += random.choice(numbers)

# Random symbols
for i in range(nr_symbols):
    password += random.choice(symbols)

# Final password after concatenating letters, numbers and then symbols
print(f"Password after contenating letters, numbers and symbols: {password}")

# Hard level
# #t8r%t9y2

password = list(password)

# Shuffling the password elements
random.shuffle(password)

print(password)

passwrd = ''
for char in password:
    passwrd += char

# Final shuffled passwords as a string
print(f"Final password after shuffling password: {passwrd}")
