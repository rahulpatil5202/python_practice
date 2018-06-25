import random

compGuess = random.randint(0,100)

while True:
    userGuess = int(input("Guess a number between 0-100:"))

    if userGuess > compGuess:
        print("Guess lower")
    elif userGuess < compGuess:
        print("Guess higher")
    else:
        print("Congrats, you've guessed it right")
        break

