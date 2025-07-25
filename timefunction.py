import time
times = int(input("Enter your time: "))

for i in range(1,times+1):
    second = i % 60
    minute = int(i / 60) % 60
    hour = int(i / 3600) %24
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("Time's up!")