# Program that automatically prints the solution to the FizzBuzz game.

for number in range(1, 101):
    if (number%3==0 and number%5==0):       # Divisible by 3 and 5 both
        print("FizzBuzz")
    elif number%3 == 0:                     # Divisible by 3 only
        print("Fizz")
    elif number%5 == 0:                      # Divisible by 5 only
        print("Buzz")
    else:
        print(number)