# Program that adds the digit in a 2 digit number

# Input - 32
# Output - 5  (3+2)

two_digit_num = input("Type a two-digit number: ")
# num = int(two_digit_num)

# first_digit = num//10
# second_digit = num%10

first_digit = int(two_digit_num[0])
second_digit = int(two_digit_num[1])


print(first_digit + second_digit)

