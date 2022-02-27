from art import logo, vs
from game_data import data
from random import choice

print(logo)

a_data = choice(data)
b_data = choice(data)

first_choice = f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}."
second_choice = f"\nCompare B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}."

print(first_choice)

print(vs)

print(second_choice)

# I have to find the way to burn the lower choice in order to don't show it again