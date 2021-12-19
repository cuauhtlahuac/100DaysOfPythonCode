#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
#For each letter in the chosen_word, add a "_" to 'display'.
for letter in chosen_word:
    display.append("_")

# TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all

user_guess = True

while user_guess:
  guess = input("Guess a letter: ")[-1].lower()
  for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = guess

  print(display)
  # the letters in the chosen_word and 'display' has no more blanks ("_").
  try:
    display.index("_")
  except:
  # Then you can tell the user they've won.
    user_guess = False
    print("You win!")
  