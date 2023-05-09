def shopping_list(budget, **kwargs):
    products = []
    if budget < 100:
        return "You do not have enough budget."

    for k, v in kwargs.items():
        if len(products) == 5:
            break

        price = float(v[0])
        quantity = int(v[1])
        total_price = price * quantity
        if total_price > budget:
            continue
        budget -= total_price
        products.append(f"You bought {k} for {total_price:.2f} leva.")

    return '\n'.join(products)



print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


# *****************

def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    basket = set()
    products = []
    for product, product_data in kwargs.items():
        if len(basket) == 5:
            break
        price = product_data[0]
        quantity = product_data[1]
        final_price = price * quantity

        if budget >= final_price:
            basket.add(product)
            products.append(f"You bought {product} for {final_price:.2f} leva.")
            budget -= final_price

    return "\n".join(products)