products = input().split(' ')
stock = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    stock[key] = int(value)

search_list = input().split(' ')
for product in search_list:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
