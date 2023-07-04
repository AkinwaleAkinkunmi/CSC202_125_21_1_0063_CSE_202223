# Treasure Island Project

print("Welcome to Treasure Island.\nYour mission is to find the treasure chest.")

way_to_go = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n>_").lower()

if way_to_go == "left":
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n>_") .lower()
    if swim_or_wait == "wait":
        door_choice = input("You arrive at the island unharmed. There is a a house with 3 doors. One red, one yellow and one blue. Which one do you choose? (r/y/b)\n>_") .lower()

        if door_choice == "y":
            print("You found a treasure chest. You win!!!")
        elif door_choice == "r":
            print("You fell into a pit of snakes. You died :(")
        elif door_choice == "b":
            print("You entered a room full of beasts. You died :(")
        else:
            print("Please pick a valid option.")

    elif swim_or_wait == "swim":
        print("You were eaten by a sea monster. Game Over:(.")
    else:
        print("Please type in a valid option.")

elif way_to_go == "right":
    print("You got lose. Game Over:(.")
else:
    print("Please pick a valid option") 
