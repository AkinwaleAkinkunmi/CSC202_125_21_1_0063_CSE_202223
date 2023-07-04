# Rock Paper Scissors
import random

print("""
Rock Paper Scissors
-------------------
""")
player_choice = input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n>_")
computer_choice = str(random.randint(0, 2))

if player_choice == "0":
    if computer_choice == "0":
        print("The computer chose rock. You draw")
    elif computer_choice == "1":
        print("The computer chose paper. You lose.")
    else:
        print("The computer chose scissors. You win!!!")
elif player_choice == "1":
    if computer_choice == "0":
        print("The computer chose rock. You win!!!")
    elif computer_choice == "1":
        print("The computer chose paper. You draw")
    else:
        print("The computer chose scissors. You lose.")
elif player_choice == "2":
    if computer_choice == "0":
        print("The computer chose rock. You lose")
    elif computer_choice == "1":
        print("The computer chose paper. You win!!!")
    else:
        print("The computer chose scissors. You draw.")
else:
    print("Please select a valid option.")

