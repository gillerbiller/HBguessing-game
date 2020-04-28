"""A number-guessing game."""
import random

playerName = input("Hello! Please enter your name ")

print (f"Hi {playerName}, I'm thinking of number between 1 and 100.")

def gamePlay():
    number = (random.choice(range(100)))
    print(number)

    guessedNumber = int(input("Pick a number. "))

    counter = 0

    for x in number:
        counter += 1
        if number < guessedNumber:
            print(input("That number is too high. Guess again. "))
        elif number > guessedNumber:
            print(input("That number is too low. Guess again "))
        else:
            number = guessedNumber
            print(f"That is the number I was thinking of! You guessed \
            it in only {counter} trys.")
        
gamePlay()



# Put your code here
