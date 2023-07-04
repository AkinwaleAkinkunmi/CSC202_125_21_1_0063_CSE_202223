# Randomization and Pyhton Lists

# Fact: Python used an algorithm called the Mersenne Twister to generate randoms.
# Importing the random module 
import random

# Random integers
random_integer = random.randint(1, 10)
# Generates a random number between 1 and 10. Where 1 and 10 are inclusive.
print(random_integer)

# Random floating numbers
random_float = random.random()
# random.random() generates a random floating number between 0 and 1. Where 1 is exclusive and 0 is inclusive.
print(random_float)

# To generate a random float number between 0 and 5, you can just multiply the .random() function by 5.
random_float_five = random.random() * 5
#This gives you a random number between 0.00000000... and 4.999999999...
print(random_float_five)

# Challenge 1 - Coin toss program
test_seed = int(input("Create a seed number:  "))
random.seed(test_seed)

heads_tails = random.randint(0, 1)
if heads_tails == 1:
    print("Heads")
else:
    print("Tails")

# Lists
# Lists are represented with square brackets []
# Indices in lists start at 0

Fruit = ["Apple", "Orange", "Mango"]
# If you want to add a new item to the list, you use the append() function.
Fruit.append("Watermelon")
print(Fruit)
# To add multiple items, you can use the extend() function.

Fruit.extend(["Guava", "Banana", "Pineapple"])
print(Fruit)

# Challenge 3 - Banker Roulette
test_seed = int(input("Create a seed number:  "))
random.seed(test_seed)
nameAsCSV = input("Give me everybody's names, separated be a comma:  ")
name = nameAsCSV.split(", ")
# split() fuction splits a string based on the criteria in the brackests and puts each of the elements inside a list.

num_items = len(name)
random_choice = random.randint(0, num_items - 1)
person_paying = name[random_choice]
print(f"{person_paying} is paying for the meal today.")

# An easier method would be to use the choice() fuction as shown below
payer = random.choice(name)
print(f"{payer} is paying for everyone's meal.")

# Challenge 4 - 
row1 = ["😁", "😁", "😁"]
row2 = ["😁", "😁", "😁"]
row3 = ["😁", "😁", "😁"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?  ")
# column before row
vertical = int(position[1])
horizontal = int(position[0])

selected_row = (map[vertical - 1])

selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
