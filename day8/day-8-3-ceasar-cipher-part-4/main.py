from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
directions = ['encode', 'decode']

# TODO-1: Import and print the logo from art.py when the program starts.

print(logo)

direction = input(
    f"Type '{directions[0]}' to encrypt, type '{directions[1]}' to decrypt:\n")
if (direction not in directions):
    print(f"please write '{directions[0]}' or '{directions[1]}'")
    exit()

d = 0 if direction == directions[0] else 1

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet_len = len(alphabet) - 1

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).

if(shift > alphabet_len):
    shift %= alphabet_len


def caesar(plain_text, shift_amount, direction):
    text_list = list(plain_text)

    for position in range(0, len(text_list)):
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"

        char = text_list[position]
        if (char not in alphabet):
            text_list[position] = char
            continue

        char_position = alphabet.index(
            char) + shift_amount if direction == directions[0] else alphabet.index(char) - shift_amount

        fix_position = char_position

        if(char_position > alphabet_len):
            fix_position = char_position - alphabet_len - 1

        text_list[position] = alphabet[fix_position]

    encoded_text = "".join(text_list)

    print(f"The {directions[d]}d text is {encoded_text}")

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.


caesar(text, shift, direction)
