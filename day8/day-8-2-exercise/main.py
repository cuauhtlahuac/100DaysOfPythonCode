# Write your code below this line ๐
def its_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def generate_primes_numbers():
    prime_list = []
    for number in range(2, 10001):
        if(its_prime(number)):
            prime_list.append(number)
    return prime_list


prime_list = generate_primes_numbers()

def prime_checker(number):
    if(number in prime_list):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
