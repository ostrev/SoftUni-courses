command = input()
dic_products = {}
while command != 'buy':
    products = command.split()
    name = products[0]
    price = float(products[1])
    quantity = int(products[2])
    if name not in dic_products:
        dic_products[name] = {}
        dic_products[name][price] = quantity
    else:
        temp_price = 0
        for k, v in dic_products[name].items():
            temp_price = float(k)
        quantity += dic_products[name].pop(temp_price)
        dic_products[name] = {price: quantity}
    command = input()
for name, value in dic_products.items():
    for price, quantity in value.items():
        print(f'{name} -> {price * quantity:.2f}')
