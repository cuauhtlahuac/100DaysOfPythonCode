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
    return menu[user_choice]
