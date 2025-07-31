# BASIC STRINGS

email = input("Enter your email: ")

# index = email.index("@")
username = email[ :email.index("@")]
domain = email[email.index("@")+1: ]

print(f"Your username is {username} and your domain is {domain}.")


#Print Each Character of a String
text = input("Enter the string: ")

for i in text:
    print(i,end = " ")