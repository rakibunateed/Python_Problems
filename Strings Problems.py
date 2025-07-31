username = input("Enter your username: ")

#check username is less than 12 character.

result = len(username)
if result > 12:
    print("Your username is to long.")
else:
    print(f"Welcome {username}.")

#Check username must not content any space.

result = username.count(" ")
if result >= 1:
    print("Username must not content any space.")
else:
    print(f"Welcome {username}.")

#Check username must not content any digit.

result = username.isalpha()
if result:
    print(f"Welcome {username}.")
else:
    print("This is invalid username, An username cannot content any digit or space.")
