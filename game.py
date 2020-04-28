"""A number-guessing game."""
import random

playerName = input("Hello! Please enter your name ")

print(f"Hi {playerName}, I'm thinking of number between 1 and 100")

number = random.choice(range(100))
print(number)
# Put your code here
