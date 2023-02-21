# Day 12 Project - Number Guessing Game
# The user will choose a difficulty level to set a fixed number of turns. To win, the user must guess the correct number between 1 and 100 in that many turns, or they will lose. 

import random
from art import logo 
  
print(logo)

print('Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.')

# A random number is chosen. 
correct_number = random.choice(range(1,101))
continue_guessing = True

#Testing code:
# print(f'Pssst, the correct answer is {correct_number}.')

# User chooses their difficulty level. 
user_choice = input('Choose a difficulty. Type "easy" or "hard": ').lower()

if user_choice == 'easy':
  num_of_guesses = 10
else:
  num_of_guesses = 5

# A function to check if the user has guessed the correct number. 
def check_answer(guess):
  if guess > correct_number:
    print('Too high.')
  elif guess < correct_number:
    print('Too low.')
  else:
    continue_guessing = False

# While loop to continue the game until the user has either guessed the correct number or run out of guesses. 
while continue_guessing:
  print(f'You have {num_of_guesses} attempts remaining.')
  user_guess = int(input('Make a guess: '))
  num_of_guesses -= 1
  check_answer(user_guess)
  if user_guess == correct_number:
    continue_guessing = False
    print(f'You got it! The answer was {correct_number}')
  elif num_of_guesses == 0:
    continue_guessing = False
    print('You\'ve run out of guesses. You lose.')
  elif num_of_guesses > 0:
    print('Guess again.')
  