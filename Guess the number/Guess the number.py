#Guess the Number Game

import random

guesses = 10
number = random.randint(1,1000)
win = False

print("Welcome to Guess the Number Game!")
print("Try in guess the number I'm thinking about.")

while guesses > 0:
    guess = int(input("Enter a number between 1 and 1000: "))

    guesses -= 1

    if guess > number:
        print("Your number was too high you have", guesses, "guesses left")
    elif guess < number:
        print("Your number was too low you have", guesses, "guesses left")
    else:
        print("You guessed the right number!")
        win = True
        guesses = 0

if win == False:
    print("You failed to guess the right number. The correct number was", number)





    

