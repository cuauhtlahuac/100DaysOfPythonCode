# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

if int(position[0]) > 3:
  raise ValueError("Maximum of the first number is 3")
first = int(position[0]) - 1

if int(position[1]) > 3:
  raise ValueError("Maximum of the second number is 3")
second = int(position[1]) - 1

map[second][first] = '💰'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")