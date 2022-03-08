# Describe the problem

def my_function():
    for i in range(1, 20):
        if i==20:
            print("You got it")
my_function()

# Here, the if condition will not run as i never gonna be equal to 20
# as the range function will run from 1 to 20(excluded). So we have to write the range(1, 21) to get the range of 20.