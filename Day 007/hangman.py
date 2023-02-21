# Day 7 Project - Hangman
# This project chooses a random word for the user to guess, letter by letter. For each guess, the code analyzes if the guessed letter is in the word or not. If it is, then it places the letter in its position in the word. If not, it draws a stage of the Hangman. The code repeats until the user wins, or until the Hangman drawing is completed and the user loses. 

from replit import clear

import random
import hangman_art
import hangman_words
#hangman_art and hangman_words were modules created by the instructor.


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code - This code was used to reveal the random word so that we could check our code.
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
  
    if guess in display:
        print(f'You have already guessed {guess}.')
      
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life')  
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Draw the stages of hangman after each wrong guess.
    print(hangman_art.stages[lives])