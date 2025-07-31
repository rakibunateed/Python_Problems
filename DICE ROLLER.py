# DICE ROLLER GAME
import random

# ● ┌ ─ ┐ │ └ ┘
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# print("┌─────────┐")
# print("│         │")
# print("│    ●    │")
# print("│         │")
# print("└─────────┘")

dice_alart = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}
dice = []
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#     for line in dice_alart.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_alart.get(die)[line],end=" ")
    print()

total =sum(dice)
print(f"Total: {total}")