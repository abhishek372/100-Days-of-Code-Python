# BMI calculator based on user's weight and height

# Inputs
height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))

# BMI calculation
bmi_value = (weight / (height**2))
bmi = round(bmi_value)

# Condition check
if bmi<18.5:
    print(f"Your bmi is {bmi}, you are Underweight")
else:
    if bmi<25:
        print(f"Your bmi is {bmi}, you have a Normal weight")
    elif (bmi>25 and bmi<30):
        print(f"Your bmi is {bmi}, you are Overweight")
    elif (bmi>30 and bmi<35):
        print(f"Your bmi is {bmi}, you are Obese")
    elif (bmi>35):
        print(f"Your bmi is {bmi}, you are Clinically obese")