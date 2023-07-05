#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Blackjack Capstone project

import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and reurns the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "You lose. Computer has blackjack"
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return " You went over. You lose"
    elif comp_score > 21:
        return "You win. The computer went over"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"

def main():
    user_cards = []
    comp_cards = []
    game_continue = True

    for i in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while game_continue:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_continue = False
        else:
            another_card = input("Do you want to draw another card? (y/n)").lower()

            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_continue = False
    while comp_score != 0 and comp_score > 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your cards: {user_cards}, your score: {user_score}")
    print(f"Computer cards: {comp_cards}, computer score: {comp_score}")
    print(compare(user_score, comp_score))  

while input("Do you want to play a game of Blackjack y/n").lower() == "y":
    main()
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




