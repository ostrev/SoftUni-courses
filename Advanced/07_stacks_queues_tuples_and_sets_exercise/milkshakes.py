from collections import deque
chocolates = [int(s) for s in input().split(', ')]
cups = [int(s) for s in input().split(', ')]

cups = deque(cups)
milkshakes = 0
while chocolates and cups and milkshakes != 5:
    chocolate = chocolates[-1]
    cup = cups[0]
    if chocolate <= 0 and cup <= 0:
        chocolates.pop()
        cups.popleft()
        continue
    if chocolate <= 0:
        chocolates.pop()
        continue
    if cup <= 0:
        cups.popleft()
        continue

    if chocolates[-1] == cups[0]:
        milkshakes += 1
        chocolates.pop()
        cups.popleft()
    else:
        cups.append(cups.popleft())
        temp = chocolates.pop()
        temp -= 5
        chocolates.append(temp)



if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
if len(chocolates) > 0:
    chocolates = [str(s) for s in chocolates]
    print(f'Chocolate: {", ".join(chocolates)}')
else:
    print('Chocolate: empty')
if len(cups) > 0:
    cups = [str(s) for s in cups]
    print(f'Milk: {", ".join(cups)}')
else:
    print('Milk: empty')