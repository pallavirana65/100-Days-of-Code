# Day 8 - Caesar Cipher Project
# Create a coded message! - Enter a message to encode, then choose a shift number. This code will shift each letter in your message by your chosen number in the alphabet to create a coded, secret message.
# To decode the message - Enter the coded message, then the shift number. This code will shift each letter backward in the alphabet by your chosen number to revewal the secret message.

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_amount, cipher_direction):
  coded_message = ''
  if cipher_direction == 'decode':
      shift_amount *= -1
  for char in input_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_char = alphabet[position + shift_amount]
      coded_message += new_char
    else:
      coded_message += char
  
  print(f'The {cipher_direction}d text is {coded_message}')


user_continue = True

while user_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26

  caesar(text, shift, direction)

  result = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()
  if result == 'no':
    user_continue = False
    print('Goodbye')