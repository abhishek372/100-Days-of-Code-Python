# Program to give us days, weeks, months we have until 90 years old using maths and f-strings.

age = input("What is your current age? ")

age_as_int = int(age)

remain_yrs = 90 - age_as_int
remain_days = remain_yrs  * 365
remain_weeks = remain_yrs  * 52
remain_months = remain_yrs  * 12

print(f"You have {remain_days} days, {remain_weeks} weeks and {remain_months} months left.")
