# Calculator program

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

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
function = operations[operation_symbol]

# Return the operation from operations
answer = function(num1, num2)

# Print the result
print(f"{num1} {operation_symbol} {num2} = {answer}")


