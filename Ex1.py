import random

low = 1
high = 100
answer = random.randint(low, high)
guesses  = 0
is_running = True

print("---Number Guessing Game---")

print(f"Select a number between {low} and {high}: ")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("That number is out of range.")
            print(f"Please select a number between {low} and {high}: ")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess.")
        print(f"Please select a number between {low} and {high}: ")
