# Task 1 sample solution
# Fizzbuzz problem.
from random import random

for num in range(1, 101):
      if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
      elif num % 3 == 0:
            print("Fizz")
      elif num % 5 == 0:
            print("Buzz")
      else:
          print(num)

# Task 2 Sample solution
import random
guesses_left = 3
random_number = random.randint(0, 10)
while guesses_left > 0:
    guess = input("Please guess a number between 1 and 10")

    if guess == random_number:
        print("Congrats! U guessed the number correctly!")
        break
    elif guess != random_number:
        print("That was wrong!")
        guesses_left = guesses_left - 1
    elif guesses_left == 3:
        print("That was wrong!")
        guesses_left = guesses_left - 1


# Task 3 sample solution
for x in range(5):
    for y in range(x):
        print("*", end="")
        print("")

for x in range(5, -1, -1):
    for x in range(x):
        print("*", end="")
        print("")



