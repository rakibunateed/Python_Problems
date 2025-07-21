age = int(input("Enter your age: "))
if age >= 18 and age <= 29:
    print("You are a adult.")
elif age < 18 and age >= 0:
    print("You are a minor.")
elif age >= 30 and age <= 49:
    print("You are in your mid 30s.")
elif age >= 50:
    print("You are in your old version.")
else:
    print("You are not born yet.")