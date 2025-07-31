# PRACTICE 2D LIST

r = int(input("Enter the number of rows: "))
c =int(input("Enter the number of columns: "))

num = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(input())
    num.append(row)

# Print the 2D list row by row
for row in num:
    for item in row:
        print(item, end=" ")
    print()
