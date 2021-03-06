# if you get over 21 you lose

# J Q and K have 10 point each

# As value is 1 or 11, for example 10 + as could be 21 or 11

# regular cards goes from 2 to 9

# if the number of both is the same, there is a draw

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from art import logo
from random import choice
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
max_score = 21

print(logo)


def getCards(num, c_list):
    n_list = c_list
    for n in range(0, num):
        n_list.append(choice(cards))
    return n_list


def calculate_score(cards):
    total = 0
    for card in cards:
        total += card

    return total


def user_lose(score):
    return score > max_score


continue_playing = True

while continue_playing:
    num_cards = 2
    play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")[0].lower()
    continue_playing = True if play == 'y' else False

    user_cards = getCards(num_cards, [])
    score = calculate_score(user_cards)
    computer_cards = getCards(num_cards, [])
    start_game = continue_playing

    while start_game:
        if 11 in user_cards and score > max_score:
          user_cards.remove(11)
          user_cards.append(1)
          score = calculate_score(user_cards)

        print(f"\n* Your cards: {user_cards}, current score: {score}")
        print(f"* Computer's first card: {computer_cards[0]}")
        print("* first user card: ", user_cards)

        if(not user_lose(score) and input("Type 'y' to get another card, type 'n' to pass: ")[0].lower() == 'y'):
            num_cards = 1
            user_cards = getCards(num_cards, user_cards)
            score = calculate_score(user_cards)
        else:
            computer_score = calculate_score(computer_cards)
            print(f"\nour final hand: {user_cards}, final score: {score}")
            print(
                f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            if(score > computer_score and score <= max_score or computer_score > max_score):
                print("you win ✅")
            elif(score > max_score and computer_score <= max_score or score < computer_score):
                print("You went over. You lose 🚩")
            else:
                print("Draw 🏳")
            start_game = False

system('clear')
print("Thanks for playing")

# our final hand: [2, 7, 5, 10], final score: 24
# Computer's final hand: [10, 10], final score: 20
# You went over. You lose 😭


##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
