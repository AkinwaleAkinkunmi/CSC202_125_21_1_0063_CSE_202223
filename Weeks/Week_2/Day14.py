# make a dictionary of the celebrities
import random
from game_data import data
from art import logo_two
from art import vs

def print_format(account):
    """This is to return print format from the account data"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}: {account_descr} from {account_country}"

def check_answer(user_guess, a_follower, b_follower):
    """Takes the user's guess and returns if they got it right"""
    if a_follower > b_follower:
        if user_guess == "a":
            return True  
        else:
            return False
    else:
        if user_guess == "b":
            return True
        else:
            return False

print(logo_two)
score = 0
playing = True

account_b = random.choice(data)

while playing:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {print_format(account_a)}")
    print(vs)
    print(f"Compare B: {print_format(account_b)}")

    # Ask user for a guess
    user_guess = input("Who has more followers? Type A or B: ").lower()

    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = check_answer(user_guess, a_follower, b_follower)

    if is_correct == True:
        score += 1
        print(f"You're right! Current score: {score} ")
    else:
        playing = False 
        print(f"Sorry, that's wrong. Final score: {score}")
    
    
# Make the game repeatable