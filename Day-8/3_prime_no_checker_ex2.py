# Program to check whether a number is prime or not

n = int(input())

def prime_checker(number):
    is_prime = True

    if number==1 or number==0:
        print(number)
    else:
        for i in range(2, number):
            if number%i == 0:
                is_prime = False
    
    if is_prime:
        print(f"{number} is prime number.")
    else:
        print(f"{number} is not prime.")

prime_checker(n)
        