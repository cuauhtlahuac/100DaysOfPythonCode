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
    for coffee in resources:
        name = str(coffee).capitalize()
        report += f"{name}: {resources[coffee]}ml\n"
    report += f"Money: ${money}"
    return report
