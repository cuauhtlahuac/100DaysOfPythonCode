# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# It's even if it is divisible by two with no remainders left 

reminder = number % 2

if reminder != 0:
  print("This is an odd number.")
else:
  print("This is an even number.")