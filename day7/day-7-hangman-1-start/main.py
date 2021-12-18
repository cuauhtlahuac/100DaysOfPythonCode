import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input(f"write a letter that you think is in the word: ")[-1]

print(f"the letter wrote was {guess}")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

if guess in chosen_word:
    print("You guessed")