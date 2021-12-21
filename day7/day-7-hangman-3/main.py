# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
    display.append("_")

user_guess = True
# You can give more live by adding a integer
lives = len(display)

while user_guess:
    guess = input("Guess a letter: ")[-1].lower()
    numberOfGuesses = 0
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            numberOfGuesses += 1

    lives -= numberOfGuesses if (numberOfGuesses > 0) else 1

    print(display, lives, numberOfGuesses)

    if lives == 0:
        print("you loose")
        user_guess = False

    # the letters in the chosen_word and 'display' has no more blanks ("_").
    try:
        display.index("_")
    except:
        # Then you can tell the user they've won.
        user_guess = False
        print("You win!")
