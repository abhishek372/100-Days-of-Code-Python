# Logical Operators
# and, or, not 

print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))
bill = 0

if height>=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age<12:
        bill = 5
        print("You have to pay $5.")
    elif (age>12 and age<18):
        bill = 7
        print("You have to pay $7.")

    # Use of logical operators
    elif (age>=45 and age<=55):
        print("Everything is going to be ok. Have a free ride on us.")
    else:
        bill = 12
        print(f"You have to pay {bill}")
    
    wants_photo = input("Do you want photo? Y or N. ")
    if wants_photo == 'Y':
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry!, you have to grow taller before you can ride.")