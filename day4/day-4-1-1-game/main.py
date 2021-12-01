import time

from time import sleep

import random

op = ["R", "P", "S"]
complete_op = {'R': 'Rock', 'P': 'Paper', 'S': 'scissors'}

separation = "-" * 15

while True:
    user_choice = input("Choice rock(R) paper(P) or scissors(S): ").upper()
    if (user_choice not in op):
        print("it's not a valid movement")
        continue
    pc_choice = random.choice(op)
    print(f"\nComputer choice {complete_op[pc_choice]}")
    sleep(0.9)

    if user_choice == pc_choice:
        print(f"\nThere is a draw, both choice {complete_op[pc_choice]}")

    elif(user_choice == op[0] and pc_choice == op[2]):
        print(f"\nYou Win!, with {complete_op[user_choice]}")

    elif(user_choice == op[2] and pc_choice == op[1]):
        print(f"\nYou Win!, with {complete_op[user_choice]}")

    elif(user_choice == op[1] and pc_choice == op[0]):
        print(f"\nYou Win!, with {complete_op[user_choice]}")

    else:
        print("\nYou loose")

    print("Game Over")
    print(separation)
    sleep(0.9)
    print("\nNew Game")
