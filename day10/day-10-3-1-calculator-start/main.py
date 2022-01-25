from art import logo

print(logo)

# add
def add(n1, n2):
    return n1 + n2

# substract
def substract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

# Create a dictionary, where we store the operation sign as key  and the operator function as value

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}


num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input('Pick an operation from the line above: ')
function = operations[operation_symbol] # here we assign the function

num2 = int(input("What's the second number?: "))

answer = function(num1, num2) # we call the function

print(f"{num1} {operation_symbol} {num2} = {answer}")

