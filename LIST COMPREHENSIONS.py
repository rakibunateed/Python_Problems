#LIST COMPREHENSIONS

# first method
n = []
for x in range(1,11):
    n.append(x*2)
print(n)

# second method
# list = [expression for values in iterable if condition]
double = [x*2 for x in range(1,11)]
triple = [x*3 for x in range(1,11)]
square = [x*x for x in range(1,11)]
print(double)
print(triple)
print(square)

fruit = ["Banana","Apple","Mango","Strawberry"]
fruit = [x.upper() for x in fruit]
print(fruit)