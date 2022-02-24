# Tip Calculator

# Greeting message
print("Welcome to the tip calculator")

# Inputs
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))


bill_with_tip = bill * (tip / 100)

# Total bill
total_bill = bill+ bill_with_tip

# Bill per person
bill_per_person = total_bill / no_of_people
bill_person = round(bill_per_person, 2)

print(f"Each person should pay: ${bill_per_person}")
