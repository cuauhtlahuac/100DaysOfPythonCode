#Number Guessing Game Objectives:
from art import logo
from random import randint
# Include an ASCII art logo.

print(logo)

number_to_guess = randint(1, 100)
min_number = 1
max_number = 100

# Allow the player to submit a guess for a number between 1 and 100.
print(number_to_guess)
user_guess = int(input(f"write a number between 1 and 100: "))

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
print (f"you win: {user_guess}") if user_guess == number_to_guess else print("Too high") if user_guess > number_to_guess else print("Too low")

# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

