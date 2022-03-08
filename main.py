import os

print("Welcome to the Auction House.")

bids = {}
def add_bid(name, bid_amount):
  bids[name] = bid_amount
  print(f"{name} successfuly placed a bid for ${bid_amount:.2f}")

def end_auction():
  highest_bid = 0
  winner = ''
  for person in bids:
    if bids[person] > highest_bid:
      highest_bid = bids[person]
      winner = person
      
  print("Auction over.")
  print(f"{winner} bid ${highest_bid:.2f} and wins the auction!")

auction_ongoing = True
while auction_ongoing:
  name = input("What is your name?\t")
  bid = float(input("How much would you like to bid?\t"))
  add_bid(name, bid)
  next_bidder = input("Are there any other bidders? (y\\n)\t".lower())
  os.system('clear')
  

  if next_bidder == 'n':
    auction_ongoing = False
    end_auction()

    