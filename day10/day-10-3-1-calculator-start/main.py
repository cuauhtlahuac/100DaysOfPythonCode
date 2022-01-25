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
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)

function = operations['+'] # here we assign the function

print(function(2,7)) # we call the function

