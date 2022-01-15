programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# retrieve the value

print(programming_dictionary["Bug"])

# adding a new value

programming_dictionary["root"] = "begining of a files tree"

print(programming_dictionary["root"])

# Loop through

for key in programming_dictionary:
    #         key         value
    print(f"{key}: {programming_dictionary[key]}")
