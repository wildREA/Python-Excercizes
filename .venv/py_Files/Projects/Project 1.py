# ------------- IMPORTS -------------
import time
import random

# ------------- VARIABLES & PROMPTS -------------
startupPrompt = "In this console game, you will have to guess a number. It will become unplayable if you guess right.\n"
# hint = "If you ever need a hint, you can call out \"/hint\"."

print(startupPrompt + "hint" + "\n")  # game info
time.sleep(5)
guess = int(input("Enter a number.\n"))  # player input
number = random.randint(0, 100)  # random integer for guessing number

# ------------- THE GAME -------------
while guess != number:
    if guess == number:
        print("You guessed correctly!")  # not sure why it doesn't work
        break  # not sure why this then works instead (same indentation)
    elif abs(guess < 0) and abs(guess > 100):  # specifies game's valid integer range
        print("guesser.Exception:valueInteger continue with input (expected (0-100)")  # input requires int within range
        guess = int(input("Enter a valid number.\n"))
    else:
        if abs(guess) > number * 1.5 or abs(guess) < number * 0.5:  # far range equation
            print("It seems you have a bit of a skill issue.")
            guess = int(input("Enter a number.\n"))
        elif abs(guess) > number * 1.2 or abs(guess) < number * 0.75:  # closer range equation
            print("You're getting closer, Hellen Keller...")
            guess = int(input("Enter a number.\n"))
        else:
            print("Careful, it's very hot!")  # close if no other range equations interrupts
            guess = int(input("Enter a number.\n"))
