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

# Create a dictionary, where we store the operation sign as value  and the operator as key

operations = {
    add: '+',
    substract: '-',
    multiply: '*',
    divide: '/'
}