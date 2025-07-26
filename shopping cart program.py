foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press q to exit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Food Cart -----")
for i in range(len(foods)):
    print(f"{foods[i]} - price is: ${prices[i]:.2f}")
total = sum(prices)
print(f"Total amount of your Food Cart is: ${total:.2f}")
