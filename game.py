"""A number-guessing game."""
import random

greeting = input("Hello! Please enter your name ")

print (f"Hi {greeting}, I'm thinking of number between 1 and 100. Try and \
guess which number I am thinking of.")

def gameplay():

    numberOfGuesses = 0

    number = (random.choice(range(1, 100)))

    while number:
        try:
            guessedNumber = int(input("Pick a number. "))
        except ValueError:
            print("Not a valid selection")
            gameplay()

        if guessedNumber < number:
            numberOfGuesses += 1
            print(f"That number is too low, {guessedNumber}")

        elif guessedNumber > number:
            numberOfGuesses += 1
            print(f"that number is too high, {guessedNumber}")

        else:
            guessedNumber == number
            print(f"That is my number! It took you {numberOfGuesses} \
guesses to guess my number.")
            break
gameplay()

