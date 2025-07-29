# random numbers
import random

high = 100
low = 1
guesses = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1

    if guess > number:
        print(f"{guess} is too high.")
    elif guess < number:
            print(f"{guess} is too low.")
    else:
        print(f"{guess} is correct!")
        break

print(f"This round took you {guesses} guesses.")