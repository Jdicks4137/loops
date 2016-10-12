# Josh Dickey 10/12/16
# This program is a simple guessing game
import random


def ask_user():
    """this asks the user whether or not you want to play"""
    user = input("Do you want to play?")
    if user == "yes":
        return True
    elif user == "no":
        print(">:(")
        return False


def select_number():
    """this has the computer select a random number"""
    return random.randint(1, 100)


def guessing(number):
    """this has the user guess the number and counts the number of tries"""
    tries = 0
    while True:
        while True:
            guess = int(input("What number am I thinking of?"))
            if guess >= 1 and guess <= 100:
                break
        if guess == number:
            print("you are correct! it took you", tries, "guesses to figure out this problem.")
            break
        elif guess >= number:
            print("you're guess is too high")
            tries += 1
        elif guess <= number:
            print("you're guess is too low")
            tries += 1


def main():
    """this is the main function that runs the program"""
    while ask_user():
        number = select_number()
        print("I am thinking of a whole number between 1 and 100")
        guessing(number)


main()
