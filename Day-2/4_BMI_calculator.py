# Create BMI calclator

# Height and weight
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# BMI
bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)

print(bmi_as_int)
