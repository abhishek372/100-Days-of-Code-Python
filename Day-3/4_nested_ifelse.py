# Nested if else statement
# Roller coaster game

# Greeting Message
print("\nWelcome to the rollercoaster!")

# Input
height = int(input("\nWhat is your height in cm? "))

# Condition check
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age<12:
        print("Please pay $5.")
    elif age>18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry!, you have to grow taller before you can ride.")
