import random

print("Welcome to the number guessing game!!!\nI am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'  ")

computer_guess = random.randint(1, 100)
def hard(computer_guess):
    attempts = 5
    while attempts != 0:
        print(f"You have {attempts} attempts to guess the number")
        player_guess = int(input("Make a guess:  "))
        if player_guess > 100 or player_guess < 1:
            print("Please make a guess from 1 to 100")
        else:
            if player_guess == computer_guess:
                print(f"You got it. The answer is {computer_guess}")
            elif player_guess > computer_guess:
                print("Too high.\nGuess again.")
                attempts -= 1
            elif player_guess < computer_guess:
                print("Too low.\nGuess again.")
                attempts -= 1
            print("You've run out of guesses, you lose")

def easy(computer_guess):
    attempts = 10
    while attempts != 0:
        print(f"You have {attempts} attempts to guess the number")
        player_guess = int(input("Make a guess:  "))
        if player_guess > 100 or player_guess < 1:
            print("Please make a guess from 1 to 100")
        else:
            if player_guess == computer_guess:
                print(f"You got it. The answer is {computer_guess}")
            elif player_guess > computer_guess:
                print("Too high.\nGuess again.")
                attempts -= 1
            elif player_guess < computer_guess:
                print("Too low.\nGuess again.")
                attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose")

if difficulty == "easy":
    easy(computer_guess)
elif difficulty == "hard":
    hard(computer_guess)