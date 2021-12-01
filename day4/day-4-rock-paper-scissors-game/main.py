rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import time

from time import sleep

import random

op = ["R", "P", "S"]
complete_op = {'R': rock, 'P': paper, 'S': scissors}

separation = "-" * 15

computer = 0

class User:
  def __init__(self):
    self.points = 0

  def add(self):
    self.points += 1


user = User()

def handle_win(choice):
  print(f"\n🏆 You Win!, with: {complete_op[choice]}")
  user.add()

while True:
    user_choice = input("Choice rock(R) paper(P) or scissors(S): ").upper()
    if (user_choice not in op):
        print("it's not a valid movement")
        continue
    pc_choice = random.choice(op)
    print(f"\n🖥  Computer choice {complete_op[pc_choice]}")
    sleep(0.9)

    if user_choice == pc_choice:
        print(f"\n🥝 There is a draw, both choice {complete_op[pc_choice]}")

    elif(user_choice == op[0] and pc_choice == op[2]):
        handle_win(user_choice)

    elif(user_choice == op[2] and pc_choice == op[1]):
        handle_win(user_choice)

    elif(user_choice == op[1] and pc_choice == op[0]):
        handle_win(user_choice)

    else:
        print(f"\n❌ You loose with: {complete_op[user_choice]}")
        computer += 1

    print("Game Over 👾 👾 👾\n")
    print(separation)
    sleep(0.9)
    print(f"\nYou {user.points} - computer {computer}")
    print("\nNew Game 👽\n")

