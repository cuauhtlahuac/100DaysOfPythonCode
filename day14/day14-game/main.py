from art import logo, vs
from game_data import data as original_data
from random import randrange
from game_utilities import win_calculator

data = original_data

final_score = 0

print(logo)

game_active = True

both_data = {}

round_number = 0
a_index = 0
b_index = 0
while game_active:
    choices = ['A', 'B']
    if round_number == 0:
      a_index = randrange(0, len(data) - 1)
      a_data = data[a_index]
    both_data[ choices[0] ] = {"data": a_data, "index": a_index}
    b_index = randrange(0, len(data) - 1, a_index)
    b_data = data[b_index]
    both_data[ choices[1] ] = {"data": b_data, "index": b_index}
    print(len(data))
    first_choice = f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}."
    second_choice = f"\nCompare B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}."

    print(first_choice)

    print(vs)

    print(second_choice)

    user_guess_char = input(f"Who has more followers? Type '{choices[0]}' or '{choices[1]}': ")[0].upper()
    choices.pop(0) if user_guess_char == choices[0] else choices.pop(1)
    user_guess = both_data[user_guess_char]
    not_selected = both_data[choices[0]]

    print(f"\nYour guess = {user_guess['data']['name']} : {user_guess['data']['follower_count']}")
    print(f"vs = {not_selected['data']['name']} : {not_selected['data']['follower_count']}")

    if(win_calculator(user_guess['data']['follower_count'], not_selected['data']['follower_count'])):
      print('\nCorrect! \n')
      final_score += 1
      a_data = user_guess['data']
      round_number += 1
      # add a data cleaner of the not selected answer
        # here, pop the index of the not selected item
      data.pop(not_selected['index'])
    else:
      print(f"\nSorry, that's wrong. Final score: {final_score}")
      game_active = False
