#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: March 28, 2022
# This is a program that generates a random number
# and the user guesses a number


import random


def main():
    # this function checks if the guess is correct\

    # generate random number
    random_variable = random.randint(1, 9)  # a number between 1 and 100

    # get the user's guess
    guess = float(input("Enter a number between 1 and 9: "))
    print("")

    # check if the user's guess is correct or incorrect
    if guess != random_variable:
        print("That is wrong!")
    else:
        print("That is correct!")


if __name__ == "__main__":
    main()
