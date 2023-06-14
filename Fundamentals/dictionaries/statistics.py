products = input().split(': ')
stock = {}

while products[0] != 'statistics':
    key = products[0]
    value = products[1]
    if key in stock:
        stock[key] += int(value)
    else:
        stock[key] = int(value)
    products = input().split(': ')
print("Products in stock:")
for (product, quantity) in stock.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(stock.keys())}')
print(f"Total Quantity: {sum(stock.values())}")