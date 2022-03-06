from coffee_resources import resources, MENU, coffee_types
from utils import show_coffee_types
print(resources["water"])
print(MENU["espresso"]["cost"])




# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # The prompt should show every time action has completed

user_choice = input(f"“What would you like? {show_coffee_types(coffee_types)}:”")

# TODO The prompt should show every time action has completed

# TODO 3. Print report.

# TODO 4. Check resources sufficient?

# TODO 5. Process coins.

# TODO 6. Check transaction successful?

# TODO 7. Make Coffee.