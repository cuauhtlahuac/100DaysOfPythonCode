from coffee_resources import resources, MENU, coffee_types
from utils import show_coffee_types, generate_report,\
                  calculate_resources, get_user_choice,\
                  process_coins

has_resources = True

# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # The prompt should show every time action has completed
while has_resources:
    user_like = input(f"What would you like? {show_coffee_types(coffee_types)}:")
    user_choice = get_user_choice(MENU, user_like)
    # TODO 3. Print report.
    if (user_like == "report"):
        print(generate_report(resources, 2.5))
        continue
    try:
        resources = calculate_resources(resources, user_choice)
    except:
        # TODO 4. Check resources sufficient?
        process_coins()
        has_resources = False


# TODO 5. Process coins.

# TODO 6. Check transaction successful?

# TODO 7. Make Coffee.