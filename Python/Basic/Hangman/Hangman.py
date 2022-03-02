from os import system, name
from words import words
import random


def citireCuvant():
    word = input("What is the word you want to use: ")
    system('cls')
    return word


def printLines(word, s):
    for x in word:
        if not(x in s):
            print("_ ", end="")
        else:
            print(x, end="")


def main():
    system("cls")
    s = ""
    gotIt = False
    word = random.choice(words)
    # print(word)
    printLines(word, s)
    nrOfGuess = 8
    while (nrOfGuess > 0) and not gotIt:
        letter = input("Letter: ")
        s = s + letter
        if letter in word:
            system('cls')
            printLines(word, s)
            print(f"\nNext")
        else:
            nrOfGuess = nrOfGuess - 1
            print(f"Wrong, you have {nrOfGuess} chances left")
        for x in word:
            if x not in s:
                gotIt = False
                break
            else:
                gotIt = True

    if gotIt:
        print("You won!!!")
    else:
        print(f"You lost!!! The word was {word}")


main()
