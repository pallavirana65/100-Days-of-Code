# Day 14 Project - Higher Lower Game
# In this game, two items will be displayed. The user must guess which item has more Instagram followers. The code will repeat and keep score until the user guesses incorrectly. 

import art
from game_data import data
import random
from replit import clear

print(art.logo)

def new_entry(entry_name):
  '''Formats the account so it is printable.'''
  new_name = entry_name['name']
  new_entry_descr = entry_name['description']
  new_country = entry_name['country']
  return f'{new_name}, a {new_entry_descr}, from {new_country}.'


game_play = True
score = 0
entry_b = random.choice(data)


while game_play:
  entry_a = entry_b
  entry_b = random.choice(data)

  #This second while loop ensures that entries A and B are not the same. 
  while entry_a == entry_b:
    entry_b = random.choice(data)
  
  print(f'Compare A: {new_entry(entry_a)}')
  print(art.vs)
  print(f'Against B: {new_entry(entry_b)}')
  guess = input('Who has more followers? Type "A" or "B": ').upper()

  # If the user guessed correctly, their score increases by one. 
  if (guess == 'A' and entry_a['follower_count'] > entry_b['follower_count']) or (guess == 'B' and entry_a['follower_count'] < entry_b['follower_count']):
    score += 1
    clear()
    print(art.logo)
    print(f'You\'re right! Current score: {score}')

  # If the user guessed incorrectly, the game is over, and their final score is displayed.
  else:
    game_play = False
    clear()
    print(art.logo)
    print(f'Sorry, that\'s wrong. Final score: {score}')

