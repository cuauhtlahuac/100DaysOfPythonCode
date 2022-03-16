def show_coffee_types(coffee_types_list):
    types_list = coffee_types_list
    formatted_coffee_types = ""
    index = 0
    for coffee in types_list:
        if index == 0:
            formatted_coffee_types += f"({coffee}/"
        elif index + 1 == len(types_list):
            formatted_coffee_types += f"{coffee})"
        else:
            formatted_coffee_types += f"{coffee}/"
        index += 1

    return formatted_coffee_types


def generate_report(resources, money):
    report = ""
    for resource in resources:
        name = str(resource).capitalize()
        report += f"{name}: {resources[resource]}ml\n"
    report += f"Money: ${money}"
    return report


def calculate_resources(resources, user_choice):
    temp_resources = resources
    for resource in temp_resources:
        temp_resources[resource] -= user_choice['ingredients'][resource]
        if temp_resources[resource] < 0:
            raise print(f"Sorry there is not enough {resource}")
    return temp_resources


def get_user_choice(menu, user_choice):
    if user_choice in menu:
        return menu[user_choice]


def process_coins():
    # Calculate the monetary value of the coins inserted.
    # E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies:
    #  =     0.25     + 0.1 x 2  + 0.05 + 0.01 x 2 = $0.52
    quarter = 0.25
    dimes = 0.1
    nickel = 0.05
    pennies = 0.001
    inserted_coins = input("Please insert coins: ")
    return

    # Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
