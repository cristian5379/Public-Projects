import random
from os import system 

maxNumber = int(input("The number will be between 1 and: "))
userNumber = 0
while userNumber < 1 or userNumber > maxNumber:
    userNumber = int(input(f"What is your number between 1 and {maxNumber}: \n"))

def computerGuess (first, last):
    guess = random.randint(first, last);
    if guess == userNumber:
        print(f"Computer got it, the number is {guess}")
        system("pause")
    elif guess < userNumber:
        print(f"The coputer guessed {guess}, it is too low")
        return computerGuess(guess, last)
    elif guess > userNumber:
        print(f"The coputer guessed {guess}, it is too high")
        return computerGuess(first, guess)

computerGuess(1, maxNumber+1)