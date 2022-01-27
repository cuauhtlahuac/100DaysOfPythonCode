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

continue_with_answer = False
want_exit = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to exit.: ")[0].lower()
if(want_exit == 'y'):
    continue_with_answer = True
while continue_with_answer:
    operation_symbol = input('Pick an operation: ')
    function = operations[operation_symbol] # here we assign the function
    num3 = int(input("What's the second number?: "))
    second_answer = function(answer, num3) # as we use the value returned we can reuse here again

    print(f"{answer} {operation_symbol} {num3} = {second_answer}")

    want_exit = input(f"Type 'y' to continue calculation with {second_answer}, or type 'n' to exit.: ")[0].lower()
    if(want_exit == 'y'):
        continue_with_answer = True
        answer = second_answer
    else:
        continue_with_answer = False
