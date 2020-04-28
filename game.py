"""A number-guessing game."""
import random

greeting = input("Hello! Please enter your name ")

print (f"Hi {greeting}, I'm thinking of number between 1 and 100.")


def gameplay():

    numberOfGuesses = 0

    number = (random.choice(range(1, 100)))
    print(number)

    while number:

        guessedNumber = int(input("Pick a number. "))

        if guessedNumber < number:
            numberOfGuesses += 1
            print(f"To low, {guessedNumber}")

        elif guessedNumber > number:
            numberOfGuesses += 1
            print(f"to high, {guessedNumber}")

        else:
            guessedNumber == number
            print(f"That is my number, you guess {numberOfGuesses} time(s)")
            break
gameplay()


  
        




# Put your code here
