# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
    display.append("_")

end_of_game = False
# You can give more live by adding a integer
lives = len(display) + 1

while not end_of_game:
    guess = input("Guess a letter: ")[-1].lower()
    numberOfGuesses = 0
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            numberOfGuesses += 1

    lives -= numberOfGuesses if (numberOfGuesses > 0) else 1

    print(display, lives, numberOfGuesses)

    # the letters in the chosen_word and 'display' has no more blanks ("_").
    if "_" not in display:
        # Then you can tell the user they've won.
        print("You win!")
        end_of_game = True
        continue

    if lives <= 0:
        end_of_game = True
        print("you loose")
        continue
