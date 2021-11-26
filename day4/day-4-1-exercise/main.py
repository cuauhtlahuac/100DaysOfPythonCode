# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random

game = input("Do you want to play Heads and Tails Y / N: ").lower()

points = 0

while game == "y":
    coin = random.randint(0, 1)
    guess = input("Guess the side of the coin H (head) T (tail): ").upper()
    if coin == 0:
        print("Head")
        if(guess == "H"):
            points += 1
            print("you guessed it right")
            game = input(
                f"Do yo want to play again? Total points = {points}: Y / N: ").lower()
        else:
            print(f"you lose, total points = {points}")
            game = "N"
    if coin == 1:
        print("Tail")
        if(guess == "T"):
            points += 1
            print("you guessed it right!")
            game = input(
                f"Do yo want to play again? Total points = {points}: Y / N: ").lower()
        else:
            print(f"you lose, total points = {points}")
            game = "N"
