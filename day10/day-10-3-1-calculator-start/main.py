from art import logo

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

def calculator():
        print(logo)
        num1 = float(input("What's the first number?: "))

        for symbol in operations:
            print(symbol)

        should_continue = True

        while should_continue:
            operation_symbol = input('Pick an operation (+ ,- ,* ,/ ): ')
            function = operations[operation_symbol] # here we assign the function

            num2 = float(input("What's the next number?: "))

            answer = function(num1, num2) # we call the function

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            num1 = answer
            if(input(f"Type 'y' to continue calculation with {answer}, or type 'n' to exit.: ")[0].lower() != 'y'):
                should_continue = False
        
        if(input(f"Type 'y' to start a new calculation or type 'n' to totally exit.: ")[0].lower() == 'y'):
            return calculator()
        else:
            print("Good bye")

calculator()
