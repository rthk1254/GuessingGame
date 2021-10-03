#guessing game
#1. random generate num from 1 - 99
#2. Every time user input will warn user guess too hot or too cold
#3. If the user answer correctly, end loop

import random as r

def guessing_game(): #define module
    answer=r.randint(0,100) #generate number from 0 - 99

    while True:
        user_guess = int(input("Please enter your answer (0-99) : "))

        if user_guess == answer:
            print("The answer is correct!")
            break
        elif user_guess > answer:
            print("Guessing too high")
        else:
            print("Guessing too low")

guessing_game()