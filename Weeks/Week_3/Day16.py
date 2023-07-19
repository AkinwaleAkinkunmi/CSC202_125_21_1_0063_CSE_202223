# OBJECT ORIENTED PROGRAMMMING
# Attributes are modeled with variables.
# Methods are modeled with functions.

# The first letter of each word in a class is capitalized.
import turtle
timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle") 
timmy.color("coral")
timmy.forward(100)


my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Lightning', 'Water', 'Fire'])
table.align = "l"

print(table)
