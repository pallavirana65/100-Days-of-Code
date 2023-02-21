# Day 5 Project - Password Generator Project
# The user chooses the number of letters, symbols and numbers they would like in a new password. This code will randomly generate a password following the user's selections. 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []

for letter in range(1, nr_letters + 1):
  x = random.choice(letters)
  password_list += x
for symbol in range(1, nr_symbols + 1):
  y = random.choice(symbols)
  password_list += y
for number in range(1, nr_numbers + 1):
  z = random.choice(numbers)
  password_list += z

random.shuffle(password_list)

password = ''
for char in password_list:
  password += char

print(f'Your password is: {password}')

