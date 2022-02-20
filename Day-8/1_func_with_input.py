# Create a greet function and call it

# Simple Function
def greet():                # Function definition
    print("Hello! Ravi")
    print("How are you?")

# call the function
greet()

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")

greet_with_name("Ronnie")

# "Ronnie" is a argument
# "name" inside function is parameter


# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"Are you living in {location}?")

# greet_with("Rahul", "Bhopal")
greet_with("Bhopal", "Rahul")       # function with positional argument

# Function with keyword arguments
def greet_as(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_as(location="Patna", name="Ashish")

# location and name are keyword arguments