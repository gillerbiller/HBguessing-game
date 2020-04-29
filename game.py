"""A number-guessing game."""
import random

greeting = input("Hello! Please enter your name ")

print (f"Hi {greeting}, I'm thinking of number between 1 and 100. Try and \
guess which number I am thinking of in only 10 guesses.")

number = (random.choice(range(1, 100)))
print(number)#for testing

#topScore = [] for when replay and topscore features are added

def gameplay():
    numberOfGuesses = 0# This needs to be in here for while loop but resets
    #due to the try/except 

    while numberOfGuesses < 10:     
        try:
            guessedNumber = int(input("Pick a number. "))
        except ValueError:
            print("Not a valid selection") 
            continue 


        if guessedNumber < number:
            numberOfGuesses += 1
            print(f"That number is too low, {guessedNumber}")
            if numberOfGuesses >= 10:
                print("Oh no, you are out of guesses!")
                break

        elif guessedNumber > number:
            numberOfGuesses += 1
            print(f"that number is too high, {guessedNumber}")
            if numberOfGuesses >= 10:
                print("Oh no, you are out of guesses!")
                break

        else:
            guessedNumber == number
            print(f"That is my number! It took you {numberOfGuesses} \
guesses to guess my number.")
            break
        
gameplay()

