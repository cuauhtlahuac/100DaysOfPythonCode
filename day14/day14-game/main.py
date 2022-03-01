from art import logo, vs
from game_data import data as original_data
from random import choice
from game_utilities import win_calculator

data = original_data

final_score = 0

print(logo)

game_active = True

both_data = {}

round_number = 0
while game_active:
    choices = ['A', 'B']
    if round_number == 0:
      a_data = choice(data)
    both_data[choices[0]] = a_data 
    b_data = choice(data)
    both_data[choices[1]] = b_data

    first_choice = f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}."
    second_choice = f"\nCompare B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}."

    print(first_choice)

    print(vs)

    print(second_choice)

    user_guess_char = input(f"Who has more followers? Type '{choices[0]}' or '{choices[1]}': ")[0].upper()
    choices.pop(0) if user_guess_char == choices[0] else choices.pop(1)
    user_guess = both_data[user_guess_char]
    not_selected = both_data[choices[0]]

    print(f"\nYour guess = {user_guess['name']} : {user_guess['follower_count']}")
    print(f"vs = {not_selected['name']} : {not_selected['follower_count']}")

    if(win_calculator(user_guess['follower_count'], not_selected['follower_count'])):
      print('\nCorrect! \n')
      final_score += 1
      a_data = user_guess
      round_number += 1
      # add a data cleaner of the not selected answer
    else:
      print(f"\nSorry, that's wrong. Final score: {final_score}")
      game_active = False
