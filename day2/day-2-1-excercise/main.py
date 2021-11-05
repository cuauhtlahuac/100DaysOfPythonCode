# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

two_strings_digits = str(two_digit_number)

if len(two_digit_number) != 2 :     
    raise Exception("Number provided must have two digits")
    
result = int(two_digit_number[0]) + int(two_digit_number[1])

print(two_strings_digits[0] + " + " + two_strings_digits[1] + " = " + str(result))
