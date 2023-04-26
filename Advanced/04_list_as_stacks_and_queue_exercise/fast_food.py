from collections import deque

food_quantity = int(input())
orders = input().split()
orders = [int(s) for s in orders]
orders = deque(orders)
print(max(orders))

while True:
    if orders:
        order_check = orders[0]
        if food_quantity - order_check >= 0:
            order = orders.popleft()
            food_quantity -= order
        else:
            break
    else:
        break
if orders:
    print('Orders left:', end=' ')
    while orders:
        print(f'{orders.popleft()}', end=" ")
else:
    print('Orders complete')



