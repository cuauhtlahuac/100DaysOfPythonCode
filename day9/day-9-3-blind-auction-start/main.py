from os import system
from art import logo
# HINT: You can call system('clear') to clear the output in the console.

bidders = []
add_other_bidder = True

print(logo)
print("\nWelcome to the secret auction program.")

while add_other_bidder:
    name = input("\nWhat is your name?: ")
    bid = int(input("\nWhat's your bid?: $"))
    bidders.append({"name": name, "bid": bid})
    add_other = input("Are there any other bidder? Type 'yes' or 'no': ")[0].lower()
    if(add_other == 'n'):
        add_other_bidder = False
    system('clear')

winner = bidders[0]["name"]
max_bid = 0
for bidder in bidders:
    if(bidder["bid"] > max_bid):
        winner = bidder["name"]
        max_bid = bidder["bid"]

print(f"The winner is {winner} with a bid of ${max_bid}")