# Primitive Data Types

#Strings

print("Hello"[-1]) # Direct access to the index of the string, it's know as substring

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# Integer

print(123 + 345)

# Float

print(3141.59)

# Boolean

True
False

num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters") * Its gonna throw a data type error

print(type(num_char)) # here its print <class 'int'>

# Changing the data type

num_char = str(num_char)

print("Your name has " + num_char + " characters") # Now tis works well