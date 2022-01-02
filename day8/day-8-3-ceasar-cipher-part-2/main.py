alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet_len = len(alphabet) - 1

def encrypt(text, shift):

  text_list = list(text)

  for position in range(0, len(text)):
      char = text_list[position]
      char_position = alphabet.index(char) + shift
      fix_position = char_position

      if(char_position > alphabet_len):
          fix_position = char_position - alphabet_len - 1

      text_list[position] = alphabet[fix_position]

  encoded_text = "".join(text_list)

  print(f"The encoded text is {encoded_text}")   

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
  text_list = list(text)

  for position in range(0, len(text)):
      char = text_list[position]
      char_position = alphabet.index(char) - shift
      fix_position = char_position

      if(char_position > alphabet_len):
          fix_position = char_position - alphabet_len - 1

      text_list[position] = alphabet[fix_position]

  encoded_text = "".join(text_list)

  print(f"The encoded text is {encoded_text}")   
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encrypt":
  encrypt(text, shift)
elif direction == "decrypt":
  decrypt(text, shift)