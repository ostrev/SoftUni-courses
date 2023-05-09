from collections import deque as dq

# orders = dq([int(s) for s in input().split(', ') if 0 < int(s) < 11])
orders = dq([int(s) for s in input().split(', ')])
employees = [int(s) for s in input().split(', ')]
total_pizzas = 0
while orders and employees:
    order = orders[0]
    if order <= 0 or order > 10:
        orders.popleft()
        continue
    employee = employees[-1]
    if order <= employee:
        total_pizzas += orders.popleft()
        employees.pop()
    else:
        orders[0] -= employee
        total_pizzas += employees.pop()

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join([str(s) for s in employees])}')

else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(s) for s in orders])}')



#******************
from collections import deque


def process_pizzas(pizzas, employees):
    total_pizzas_count = 0
    while pizzas and employees:
        while pizzas[0] > employees[-1]:
            total_pizzas_count += employees[-1]
            pizzas[0] = pizzas[0] - employees[-1]
            employees.pop()

            if not pizzas or not employees:
                return total_pizzas_count

        total_pizzas_count += pizzas.popleft()
        employees.pop()
    return total_pizzas_count


pizzas = deque([int(el) for el in input().split(", ") if 0 < int(el) < 11])
employees = [int(el) for el in input().split(", ")]

total_pizzas_count = process_pizzas(pizzas, employees)

if pizzas:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizzas])}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_count}")
    print(f"Employees: {', '.join([str(el) for el in employees])}")


# ***************
from collections import deque

pizza_orders = deque(int(x) for x in input().split(', ') if 0 < int(x) < 11)
employees = deque(int(x) for x in input().split(', '))

total_pizzas = 0
while pizza_orders and employees:
    order = pizza_orders.popleft()
    employee = employees.pop()

    total_pizzas += min(employee, order)

    if order > employee:
        order -= employee
        pizza_orders.appendleft(order)

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(el) for el in pizza_orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(el) for el in employees)}")
    