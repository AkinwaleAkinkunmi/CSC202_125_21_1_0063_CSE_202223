# Functions with input
import math
def greet():
    print("Hello")
    print("World")
    
greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Wale")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with(name = "Wale", locaton = "Lagos")

# Challenge 1 -  Wall painting

def area_calc(height, width, cover):
    area = height * width
    no_of_cans = math.ceil(area / cover)
    print(f"You will need {no_of_cans} cans of paint.")

test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall: "))
coverage = 5


area_calc(height = test_h, width = test_w, cover = coverage)

# Challenge 2 - Prime number checker
def prime_check(number):
    is_prime = True
    for i in range(2,number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")
            

num = int(input("Number: "))
prime_check(number = num)
    