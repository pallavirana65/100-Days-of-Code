# Day 4 Project - Rock, Paper, Scissors
# The user plays Rock, Paper, Scissors against the computer. The user chooses either Rock, Paper, Scissors first. This code will then make a random choice for the computer, then generate the result. 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

game_images = [rock, paper, scissors]

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))

computer = random.randint(0, 2)

if choice >= 3 or choice < 0:
  print('You typed an invalid number. You lose.')
else:
  print(game_images[choice])

  print('Computer chose:')

  print(game_images[computer])


  if choice == 0 and computer == 2:
    print('You win!')
  elif computer == 0 and choice == 2:
    print('You lose.')
  elif choice > computer:
    print('You win!')
  elif computer > choice:
    print('You lose.')
  elif choice == computer:
    print('It\'s a draw.')
  