import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 10)

# Ask the user again and again until guess is correct
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        print("Correct🎉 You guessed the number!")

print("Game Over!")
