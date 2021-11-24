# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").upper()
name2 = input("What is their name? \n").upper()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total = 0

total += name1.count('T') + name2.count('T')
total += name1.count('R') + name2.count('R')
total += name1.count('U') + name2.count('U')
total += name1.count('E') + name2.count('E')
total1 = str(total)

total = 0

total += name1.count('L') + name2.count('L')
total += name1.count('O') + name2.count('O')
total += name1.count('V') + name2.count('V')
total += name1.count('E') + name2.count('E')

total2 = str(total)

loveScore = total1 + total2

loveNumber = int(loveScore)

# For Love Scores less than 10 or greater than 90, the message should be:
if loveNumber < 10 or loveNumber > 90:
  responseOne = f"Your score is {loveScore}, you go together like coke and mentos."
  print(responseOne)

# For Love Scores between 40 and 50, the message should be:
elif loveNumber > 40 and loveNumber < 50:
  responseTwo = f"Your score is {loveScore}, you are alright together."
  print(responseTwo)
# Otherwise, the message will just be their score. e.g.:
else:
  responseThree = f"Your score is {loveScore}."
  print(responseThree)

