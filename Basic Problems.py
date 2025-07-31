import time

#NEGATIVE & POSITIVE
num = int(input("Enter your number: "))
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

#ODD EVEN
if num & 1:
    print(f"{num} is Odd!")
else:
    print(f"{num} is Even!")

#ODD EVEN SUBPROBLEM
n = int(input())
if n % 2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")

#Print all even numbers between 1 and N.
n = int(input("Enter an number: "))
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#Print Multiplication Table
n =int(input("Enter an number: "))
for i in range(1,11):
    print(i,f"X {n} =",i*n)

# FIND THE TIME
times = int(input("Enter your time: "))
for i in range(1,times+1):
    second = i % 60
    minute = int(i / 60) % 60
    hour = int(i / 3600) %24
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("Time's up!")