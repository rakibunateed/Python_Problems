#MEMBERSHIP OPERATORS PROBLEM

email = "rakibunateed@gmail.com"

if "@" in email and "." in email:
    print("Valid email!")
else:
    print("Invalid email!")

grade = {"atied" : "A+",
         "ramim": "A",
         "rakib": "B-"}

student =input("Enter name of student: ")

if student in grade:
   print(f"{student}'s grade is {grade[student]}")
else:
     print(f"{student} was not a student!")

