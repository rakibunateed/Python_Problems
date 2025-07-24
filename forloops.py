#print number 1 to 10

for i in range(1,11):
    print(i)

#Take an integer n from the user and print the sum of numbers from 1 to n.

n = int(input("Enter the number: "))
sum = 0
for i in range(1,n):
    sum+= i

print(f"The total sum of number 1 to n is: {sum}")
