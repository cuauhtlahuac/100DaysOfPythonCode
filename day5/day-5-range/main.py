for number in range(1, 10): # not including 10
  print(number)

for number in range(1, 11, 3): # in each third iteration it will print the number
  print(number)

# Print the sum all the number between 1 and 100 

total_sum = 0

for number in range(1, 101):
  total_sum += number

print(total_sum) # expected result 5050
