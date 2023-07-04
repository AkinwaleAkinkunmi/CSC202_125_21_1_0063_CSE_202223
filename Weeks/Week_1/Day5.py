# Loops
# Python has the "for" loop and the "while" loop.

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Challenge 1 - Average Height without the len and sum fuction

student_heights = input("Input a list of student heights  ") .split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height

num_of_students = 0
for student in student_heights:
    num_of_students += 1

average = round(total_height / num_of_students)
print(average)

# Challenge 2 - Highest Score

student_scores = input("Input a list of student scores:  ") .split()
for n in range (0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")

# For loops in range function
for number in range(1, 10):
#Where 10 is exlusive and 1 is inclusive
   print(number)
#If you want to add an interval
for number in range(1, 10, 2):
#Takes intervals in 2s
   print(number)

# Challenge 3 - Adding even numbers

total = 0
for num in range(2, 101, 2):
    total += num
print(total)

# Challenge 4 - Fizz Buzz
for num in range(1, 101):
    if num % 3 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
       print("Buzz")
    else:
        print(num)