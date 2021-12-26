import random
from time import sleep

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
    display.append("_")

# You can give more live by adding a integer
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ")[-1].lower()
    n_char_guessed = 0
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            n_char_guessed += 1

    if (n_char_guessed < 1):
        lives -= 1
        print(stages[lives])

    print(display, lives, n_char_guessed)

    # the letters in the chosen_word and 'display' has no more blanks ("_").
    if "_" not in display:
        # Then you can tell the user they've won.
        print("\nYou win! 🏆\n")
        end_of_game = True
        sleep(2)
        continue

    if lives <= 0:
        end_of_game = True
        print("\nyou loose 😵\n")
        sleep(2)
        continue
 