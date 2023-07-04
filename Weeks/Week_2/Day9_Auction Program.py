#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Auction game
print("Welcome to a secret auction game.")

bidder = {}
bidding = True 

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")           
while bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidder[name] = bid
    continue_bid = input("Are there any other bidders? y/n ").lower()
    
    if continue_bid == "n":
        bidding = False
        print("All biddings have been entered.")
        highest_bidder(bidder)

        
        


# In[ ]:





# In[ ]:




