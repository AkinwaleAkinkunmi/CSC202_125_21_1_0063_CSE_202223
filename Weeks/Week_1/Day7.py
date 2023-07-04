# Hangman
#Step 1 

import random


from Hangman_words import word_list

random_word = random.choice(word_list)
word_length = len(random_word)
display = []
playing = True

lives = 6

from Hangman_art import logo, stages

print(logo)
print(f"The solution is {random_word}") #Testing purposes

for _ in range(word_length):
    display.append("_")
print(display)

while playing:
    player_choice = input("Guess a letter\n>_") .lower()

    if player_choice in display: 
        print(f"You've already guessed {player_choice}")

    for position in range(word_length):
        letter = random_word[position]
        if letter == player_choice:
            display[position] = letter
    print (f"{''.join(display)}")

    if player_choice not in random_word: 
        print(f"You guessed {player_choice}, that's not in the mystery word. You lose a life.")
        lives -= 1
        if lives == 0:
            playing = False
            print("You Lose")

    if "_" not in display:
        playing = False
        print("You win")

    print(stages[lives])


