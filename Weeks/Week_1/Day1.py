# Classic "Hello World"
print("Hello World!")

# Chellenge 1 - Printing lines of code
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Multiple Print Lines
print("Hello world!\nHello world!\nHello world!")

# String concatenating
print("Hello" + " Wale")

# Challenge 2 - Debugging lines of code 
# Line 1-print(Day 1 - Sring Manipulator)
print("Day 1 - String Manipulatlor")
#Line 2-print("Sting Concatenating is done with the"+" sign.")
print("String Concatenation is done with the '+' sign")
#Line 3- print('e.g. print("Hello " + "world")') 
print('e.g. print("Hello " + "world")')
# Line 4-print(("New lines can be created with backlash and n.")
print("New lines can be created with backlash and n.")

# Input Function
print("Hello " + input ("What is your name?") + "!")

# Challenge 3 - Print the number of characters of your inputed name 
print(len(input("What is your name?")))
# The len() function is used to print the length of string characters

# Variables
# Solving challenge 3 but with the use of variables
name = input("What is your name?")
length = len(name)
print(length)

# Challenge 4 - Switching the values stored in 2 different variables
 
a = input("a: ")
b = input("b: ")
# assign a to another separate variable
new = a
# assign b to a so that whatever is on a will be over written by whatever is on b
a = b
# notice that variable new and a were the same so since a has been overwritten by b, we can make use of the variable new and assign it to b 
b = new
print("a = " + a)
print("b = " + b)

# When naming your variables, you have to make your variable name understandable
# If you want your variable name to contain 2 different words, you separate those words with an underscore(_)
# e.g. Snake_case = 2
# Don't use numbers or symbols to start your variable's name 
# Don't use key words like print and inout to name your variables.
