# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

current_years = 90 - int(age)

days_in_a_year = 365.6
weeks_in_a_year = 52
months_in_a_year = 12

days = int(current_years * days_in_a_year)
weeks = current_years * weeks_in_a_year
months = current_years * months_in_a_year

message = f"You have {days} days, {weeks} weeks, and {months} months left." # is like Template strings in js

print(message)