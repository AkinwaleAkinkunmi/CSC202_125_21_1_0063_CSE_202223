# Conditional Statements, Logical Operators, Code Blocks and Scope

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?  "))

# Syntax for a conditional statement
if height >= 120:
    print("You can ride!")
else:
    print("You aren't tall enough to take this ride. :(")

# You use '==' to check if the value on the left is EQUAL to the value on the right
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?  "))

if height == 120:
    print("You can make this ride ")
else:
    print("Sorry you can't take this ride")

# Challenge 1 - Check if a number is even or odd

number = int(input("What number do you want to check for?  "))

remainder = number % 2
# The % sign above is an arithmetic operation called Modulo which calculates the remainder after dividing the value on the left side by the value on the right side. 
if remainder == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")

# Nested if Statements and Elif statements
# Nested if statements have if statements inside the if statements
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?  "))

if height >= 120:
    print("You can take this ride!")
    age = int(input("How old are you?  "))

    if age > 18:
        print("You will pay 12 dollars for your ticket")
# elif statements if you want to check for more than 1 conditions 
    elif age >= 12 and age <= 18:
        print("You will pay 7 dollars for your ticket")
    else:
        print("You will pay 5 dollars for your ticket")
else:
    print("You are not tall enough for this ride")

# Challenge 2 - Upgraded BMI Calculator

weight = float(input("What is your weight in kg?  "))
height = float(input("What is your height in m?  "))

BMI = weight/(height ** 2)
BMI_round = round(BMI, 1)


if BMI_round < 18.5:
    print(f"Your BMI is {BMI_round}, you are underweight")
elif BMI_round > 18.5 and BMI_round < 25:
    print(f"Your BMI is {BMI_round}, you are normal weight")
elif BMI_round > 25 and BMI_round < 30:
    print(f"Your BMI is {BMI_round}, you are overweight")
elif BMI_round > 30 and BMI_round < 35:
    print(f"Your BMI is {BMI_round}, you are obese")
else:
    print(f"Your BMI is {BMI_round}, you are clinically obese")
 
# Challenge 3 - Check if a given year is a leap year

year = int(input("What year do you want to check?  "))

leap_year = year % 4
hundreth = year % 100
four_hundreth = year % 400
if leap_year == 0:
    if hundreth == 0:
        if four_hundreth == 0:
            print(f"The year, {year} is a leap year")
        else:
            print(f"The year, {year} is not a leap year")
    else:
        print(f"The year, {year} is not a leap year")
else:
    print(f"The year, {year} is not a leap year")

# Multiple if statements in succession

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?  "))

bill = 0

if height >= 120:
    print("You can take this ride!")
    age = int(input("How old are you?  "))
    
    if age > 18:
        bill = 12
        print("You will pay 12 dollars for your ticket")

    elif age >= 12 and age <= 18:
        bill = 7
        print("You will pay 7 dollars for your ticket")

    else:
        bill = 5
        print("You will pay 5 dollars for your ticket")
    
    wants_photo = input("Do you want your photo taken? It will cost you an extra 3 dollars. (y/n)") .lower()
#    The .lower() is to change the input the user to lowercase gives even if he input an uppercase letter
    if wants_photo == "y":
        bill += 3
    
    print(f"Your final bill is {bill} dollars. Have a nice ride.")
else:
    print("You are not tall enough for this ride")

# Challenge 3 - Pizza Order

print("Welcome to pizza deliveries")
size = input("What size of pizza do you want? S, M or L  ") .upper()
add_pepperoni = input("Do you want pepperoni? Y or N  ") .upper()
extra_cheese = input("Do you wanrt extra cheese? Y or N   ") .upper()

bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
else:
    print("Choose a valid option")
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}.")

# Logical Operators
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?  "))

bill = 0
if height >= 120:
    print("You can take this ride!")
    age = int(input("How old are you?  "))

    if age >= 45 and age <= 55:
        bill = 0
        print("Your ride is free!!!")
    elif age > 18:
        bill = 12
        print("You will pay 12 dollars for your ticket")

    elif age >= 12 and age <= 18:
        bill = 7
        print("You will pay 7 dollars for your ticket")


    elif age > 18:
        bill = 5
        print("You will pay 5 dollars for your ticket")
    

    else:
        print("Enter a valid answer")
    
    wants_photo = input("Do you want your photo taken? It will cost you an extra 3 dollars. (y/n)  ") .lower()

    if wants_photo == "y":
        bill += 3
    
    print(f"Your final bill is {bill} dollars. Have a nice ride.")
else:
    print("You are not tall enough for this ride")

# Challenge 4 - Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n>_")
name2 = input("What is their name?\n>_")

print("""
T    L
R    O
U    V
E    E
------
"""
)

combined_name = name1 + name2
lower_combined_name = combined_name .lower()

t_occur = lower_combined_name .count("t")
r_occur = lower_combined_name .count("r")
u_occur = lower_combined_name .count("u")
e_occur = lower_combined_name .count("e")

print(f"T occurs {t_occur} times")
print(f"R occurs {r_occur} times")
print(f"U occurs {u_occur} times")
print(f"E occurs {e_occur} times")

true_total_occur = t_occur + r_occur + u_occur + e_occur

print(f"Total = {true_total_occur}")

string_true = str(true_total_occur)

l_occur = lower_combined_name .count("l")
o_occur = lower_combined_name .count("o")
v_occur = lower_combined_name .count("v")

print(f"L occurs {l_occur} times")
print(f"O occurs {o_occur} times")
print(f"V occurs {v_occur} times")
print(f"E occurs {e_occur} times")

love_total_occur = l_occur + o_occur + v_occur + e_occur

print(f"Total = {love_total_occur}")

string_love = str(love_total_occur)

true_love = string_true + string_love

int_true_love = int(true_love)

if int_true_love < 10 or int_true_love > 90:
    print(f"Your score is {int_true_love}, you go together like coke and mentos.")
elif int_true_love > 40 and int_true_love < 50 :
    print(f"Your score is {int_true_love}, you are alright together.")
else:
    print(f"Your score is {int_true_love}.")
    