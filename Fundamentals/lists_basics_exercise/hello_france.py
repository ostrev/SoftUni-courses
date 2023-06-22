collection_items = input().split('|')
budget = float(input())
bought_items_price = []
profit = 0
for item in collection_items:
    if 'Clothes' in item:
        item = item.split('->')
        price = float(item[1])
        if price <= 50 and budget >= price:
            budget -= price
            profit += ((price * 1.4) - price)
            bought_items_price.append(price * 1.4)
    elif 'Shoes' in item:
        item = item.split('->')
        price = float(item[1])
        if price <= 35 and budget >= price:
            budget -= price
            profit += ((price * 1.4) - price)
            bought_items_price.append(price * 1.4)
    elif 'Accessories' in item:
        item = item.split('->')
        price = float(item[1])
        if price <= 20.50 and budget >= price:
            budget -= price
            profit += ((price * 1.4) - price)
            bought_items_price.append(price * 1.4)


for i in bought_items_price:
    print(f'{i:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')

if sum(bought_items_price) + budget > 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
