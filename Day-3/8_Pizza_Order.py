# Pizza Order program

print("\nWelcome to Python Pizza Deliveries")

# Inputs
size = input("\nWhat size pizza do you want? S, M or L. ")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
extra_cheese = input("Do you want extra cheese? ")

# Bill 
bill = 0

# Conditions check for size
if size=="S":
    bill += 15 
elif size=="M":
    bill += 20
elif size=="L":
    bill += 25

# Condition check for add_pepperoni
if add_pepperoni=="Y":
    if size=="S":
        bill += 2
    else:
        bill +=3

# Condition check for extra_cheese
if extra_cheese=="Y":
    bill += 1

print(f"\nYour final bill is {bill}.")
