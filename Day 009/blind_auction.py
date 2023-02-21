# Day 9 - Blind Auction Project
# This code allows multiple users to enter in their bids for an item. Bidding is private, as the code will clear the previous bid before the next person can submit their bid. Once all participants have entered their bids, the code will return the name and bid of the winner. 

from replit import clear

from art import logo
print(logo)

num_of_bids = {}

bidding_finished = False

def find_highest_bid(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f'The winner is {winner} with a bid of ${highest_bid}!')

while not bidding_finished:
  bidder_name = input('What is your name? ')
  bidder_price = int(input('What is your bid? $'))
  num_of_bids[bidder_name] = bidder_price
  other_bids = input('Are there any other bidders?\n').lower()
  if other_bids == 'no':
    bidding_finished = True 
    clear()
    find_highest_bid(num_of_bids)
  elif other_bids == 'yes':
    clear()