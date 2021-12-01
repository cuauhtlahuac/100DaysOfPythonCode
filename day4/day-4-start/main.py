import random
import my_module

new_int = random.randint(1, 10)
print(new_int)

random_float = random.random() # It's generate floating numbers between 0.0 and a number before 1.0
print(random_float)

random_float * 5 # here we have a trick to get a random number between 0 and 5 
                 # because the multiplication with floating numbers never gonna reach the 5
                 # for example 0.99999 * 5 is equal to 4.999995

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}") # easy way to do a previous game