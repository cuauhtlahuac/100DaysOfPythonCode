# 🚨 Don't change the code below 👇
from typing import final


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").capitalize()
add_pepperoni = input("Do you want pepperoni? Y or N: ").capitalize()
add_extra_cheese = input("Do you want extra cheese? Y or N: ").capitalize()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

final_bill = 0

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_small = 2
pepperoni_medium = 3

extra_cheese = 1

if(size == "S"):
  final_bill += small_pizza
if size == "M":
  final_bill += medium_pizza
if size == "L":
  final_bill += large_pizza

if(add_pepperoni == "Y"):
  if(size == "S"):
    final_bill += pepperoni_small
  else:
    final_bill += pepperoni_medium

if add_extra_cheese == "Y":
  final_bill += extra_cheese

print(f"Your final bill is: ${final_bill}.")