# BASICS OF LOOPS

name = input("Enter your full name : ")

while name == "":
    print(f"This is the incorrect username {name}.")
    name = input("Please reenter your name: ")

print(f"Welcome {name}.")

num = int(input("Enter an number between 0-10: "))

while num < 1 or num > 10:
    print(f"{num} is an incorrect number.")
    num = int(input("Enter another number between 0-10: "))

print(f"{num} is the correct number.")
