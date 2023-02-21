# Day 2 Project - Tip Calculator
# This project asks the user to enter in their bill ammount, tip amount, and the number of people in the party. The code will use that information to split the bill, including tip, evenly and generate the amount each person should pay. 


print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

payment = round((bill + (bill * (tip / 100))) / people, 2)

print(f'Each person should pay: ${payment}')