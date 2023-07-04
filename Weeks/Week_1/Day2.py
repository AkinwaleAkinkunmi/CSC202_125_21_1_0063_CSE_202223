# Subscripting a string
# Use square brackets to indicate the index of a string 
# Indices start from 0
print("Hello"[4])

# Anything that is inside a quote is treated as a string data type in python
# The most common number data type is integer

# You can use underscore to separate number in python e.g. 100,000 can be written as 100_000
# Float datatypes are decimal numbers

# Boolean datatypes have only two possible values: True and False
# Note that both the T in True and the F in False are capitalized.

# To check the data type of data you use the type() function
# e.g. 
print(type(123))

# Data Conversion
num_char = len(input("What is your name?"))
# If you want to convert num_char to a string you use the str()
new_num_char = str(num_char)
# So new_num_char is now a string 
# This is used if you want to concatenate a string and an integer
# Since python doesn't allow that you can convert that integer to string as done below
print("Your name has " + new_num_char + " characters.")

# You can also use the float() to convert to float and int() to conver to integer.
print (70 + float("100.5"))

# Challenge 1 - Input a random two digit number and the computer would add the first and the second number together and print the sum as an integer

# Input your number
num = input("Enter a two digit number:  ")

# Since the input type above is a string, you can subscript it and assign the two different parts to a variable
first_num = num[0]
second_num = num[1]

# Convert those strings to integer and assign them to a new variable
int_first_num = int(first_num)
int_second_num = int(second_num)

# Add the variables
print(int_first_num + int_second_num)

# Mathematical Operations are addition(+), subtarction(-), multiplication(*), division(/), exponent(**)
# Note that divisions are always in float
# Python follows the PEMDAS(Parenthesis Exponent Multiplication Division Addition Subtraction )

# Challenge 2 - Working out a person's Body Mass Index based on his wight and height

weight = float(input("What is your weight?  "))
height = float(input("What is your height?  "))

BMI = weight/(height ** 2)
BMI_int = int(BMI)
BMI_string = str(BMI_int)

print("Your Body Mass Index is " + BMI_string + ".")

# Rounding Numbers
# To round numbers you use the round()

print(round(10/3, 2))

# The 2 there is the number of decimal places you want to round to 
# When rounding to a whole number, you don't need the second number

# If you want your division result to be in an integer data type, the shortcut is to use the '//'
print(10 // 3)

# F-strings can be used to concatenate different data types
print(f"Your score is {12}")

# Challenge 3 - Life in weeks, days and months if we live up to 90
age = int(input("What is your current age?  "))
remaining_age = 90 - age

weeks = 52 * remaining_age
days = 365 * remaining_age
months = 12 * remaining_age

print(f"You have {days} days, {weeks} weeks and {months} months left.")




