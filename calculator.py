# CREATING A CALCULATOR

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter an operatior(+,-,*,/): ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(abs(num1 - num2))
elif operator == '*':
    print(num1 * num2)
else:
    print(round(num1/num2))
