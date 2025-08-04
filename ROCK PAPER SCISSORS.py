# ROCK PAPER SCISSORS PROGRAM
import random


options = ("Rock","Paper","Scissors")

running = True
player = input("Enter your choice (Rock, Paper, Scissors): ")
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter your choice (Rock, Paper, Scissors): ")

    print("-----------------------")
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    print("-------- WINNER --------")
    if player == computer:
        print("It's a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
    elif player == "Paper" and computer == "Rock":
        print("You win!")
    elif player == "Scissors" and computer == "Paper":
        print("You win!")
    else:
        print("You Loss!")
    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False