from collections import deque as dq


customers = dq([int(s) for s in input().split(', ')])
taxis = [int(s) for s in input().split(', ')]
total_time = 0
while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]

    if taxi >= customer:
        total_time += customer

        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f"Customers left: {', '.join([str(s) for s in customers])}")

