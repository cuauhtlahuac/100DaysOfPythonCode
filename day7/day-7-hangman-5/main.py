import random
import os
from time import sleep
from hangman_art import stages, logo, thanks
from hangman_words import word_list


def clear_console():
    os.system('clear')


def write_display(display):
    return " ".join([str(item) for item in display])


def update_letters_chosen(letters, letter):
    return letters + letter


def update_letters_to_display(letters):
    display = ""
    index = 0
    for letter in letters:
        if(index >= 3):
            display += "\n" + " " * 8
            index = 0
        display += f"[ {letter} ]"
        index += 1
    return display


new_game = True
while new_game:
    print(logo)
    sleep(2)
    end_of_game = False
    chosen_word = random.choice(word_list)
    display = []
    letters_chosen = ""
    letters_chosen_display = ""

    for letter in chosen_word:
        display.append("_")

    # You can give more live by adding a integer
    lives = 6

    while not end_of_game:
        emoji = "🙌"
        try:
            guess = input("\nGuess a letter: ")[-1].lower()
        except:
            print("It's looks that is not a word, please write a know char")
            continue

        if guess in letters_chosen:
            print(f'\nYou\'ve already guessed "{guess}"')
            print("_" * 49 + " 🤓 " + "_" * 49)
            continue

        n_char_guessed = 0

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess
                n_char_guessed += 1

        if (n_char_guessed < 1):
            lives -= 1
            print(f'\n"{guess}" is not in the word. You lose a life.')
            emoji = "😦"
            print(f'{stages[lives]}')

        letters_chosen = update_letters_chosen(letters_chosen, guess)
        letters_chosen_to_display = update_letters_to_display(letters_chosen)

        print("LETTERS", letters_chosen_to_display)
        print("\n")
        print(write_display(display))

        print(f"\nYou have {lives} lives")
        print("_" * 49 + f" {emoji} " + "_" * 49)

        # the letters in the chosen_word and 'display' has no more blanks ("_").
        if "_" not in display:
            # Then you can tell the user they've won.
            end_of_game = True
            print("\nYou win! 🏆\n")
            sleep(1)
            choose = input(
            "would you like to start a new game? y or n  ")[-1].lower()
            if choose != "y":
                new_game = False
                print(thanks)
                sleep(2)
            clear_console()
            sleep(1)
            continue
            continue

        if lives <= 0:
            end_of_game = True
            print("\nyou loose 😵\n")
            print(f"The word was: {chosen_word}!  🐵\n")
            sleep(2)
            choose = input(
                "would you like to start a new game? y or n  ")[-1].lower()
            if choose != "y":
                new_game = False
                print(thanks)
                sleep(2)
            clear_console()
            sleep(1)
            continue
