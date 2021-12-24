import random
import os
from time import sleep
from hangman_art import stages, logo
from hangman_words import word_list

def clear_console ():
    os.system('clear')

print(logo)
sleep(2)

end_of_game = False
chosen_word = random.choice(word_list)
display = []

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
    display.append("_")

# You can give more live by adding a integer
lives = 6

while not end_of_game:
    guess = input("\nGuess a letter: ")[-1].lower()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"\nYou already wrote this letter: {guess}")
        continue
    
    n_char_guessed = 0
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            n_char_guessed += 1

    if (n_char_guessed < 1):
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f'\n"{guess}" is not in the word. You lose a life.')
        print(f"\n{stages[lives]}")



    print("\n")
    print(display)
    print("\n ")

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

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
