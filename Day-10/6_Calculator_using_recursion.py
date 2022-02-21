# Calculator program - Here we want to call the calculator function from start

from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def mul(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add, 
    "-" : sub,
    "*" : mul,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:    
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        choice = input(f"Tap 'y' to continue calculating with {answer}, or type 'n' to start again fresh.: ")

        if choice == 'y':
            should_continue = True
            num1 = answer
        else:
            should_continue = False
            calculator()                       # call the function itself - recursion


# Calling the function
calculator()