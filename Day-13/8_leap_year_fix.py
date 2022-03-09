# year = input("Which year do you want to check?")

year = int(input("Which year do you want to check?"))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not Leap year.")

# Here, in line 1,  year is string and it should be converted into the integer to compare
