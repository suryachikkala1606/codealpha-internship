stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0

print("Available Stocks:")
for stock, price in stocks.items():
    print(stock, "-", price)

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    name = input("Enter stock name: ").upper()

    if name in stocks:
        quantity = int(input("Enter quantity: "))
        total += stocks[name] * quantity
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total}")

print("Result saved in portfolio.txt")