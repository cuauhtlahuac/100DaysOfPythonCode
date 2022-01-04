alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
directions = ['encode', 'decode']

direction = input(
    f"Type '{directions[0]}' to encrypt, type '{directions[1]}' to decrypt:\n")
if (direction not in directions):
    print(f"please write '{directions[0]}' or '{directions[1]}'")
    exit()

d = 0 if direction == directions[0] else 1

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet_len = len(alphabet) - 1

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(plain_text, shift_amount, direction):
    text_list = list(plain_text)

    for position in range(0, len(text_list)):
        char = text_list[position]

        char_position = alphabet.index(
            char) + shift_amount if direction == directions[0] else alphabet.index(char) - shift_amount

        fix_position = char_position

        if(char_position > alphabet_len):
            fix_position = char_position - alphabet_len - 1

        text_list[position] = alphabet[fix_position]

    encoded_text = "".join(text_list)

    print(f"The {directions[d]}d text is {encoded_text}")

caesar(text, shift, direction)
