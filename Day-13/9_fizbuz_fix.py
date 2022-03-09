# for number in range(1, 101):
#     if number%3 == 0 or number%5 == 0:
#         print("FizzBuzz")
#     if number%3 == 0:
#         print("FIzz")
#     if number%5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# In above code, line 1, it should be 'and' in place of 'or' 
# And, it should be elif after first if till else statement.



for number in range(1, 101):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)
    