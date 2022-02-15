# Number Guessing Game Objectives:
from traceback import print_tb
from art import logo
from random import randint

# Include an ASCII art logo.
print(logo)

number_to_guess = randint(1, 100)
min_number = 1
max_number = 100

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
difficulties = {
    "easy": 10,
    "hard": 5
}

# Allow the player to submit a guess for a number between 1 and 100.
print(number_to_guess)
print(f"i'm thinking of a number between 1 and 100: ")
difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard: ")
attempts = difficulties[difficulty]

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    user_guess = int(input(f"Make a guess: "))

    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    # If they got the answer correct, show the actual answer to the player.
    if user_guess == number_to_guess:
        print(f"you win 🥇: {user_guess}")
        attempts = 0
        continue

    # Track the number of turns remaining.
    # If they run out of turns, provide feedback to the player.
    if user_guess > number_to_guess:
        print("Too high ⬆")
    else:
        print("Too low ⬇")
    attempts -= 1

    print(f"You lose ❌, the number is: {number_to_guess}") if attempts == 0 else 0
