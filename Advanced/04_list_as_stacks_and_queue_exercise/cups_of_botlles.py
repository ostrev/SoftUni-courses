from collections import deque
cups = [int(s) for s in input().split()]
bottles = [int(s) for s in input().split()]
cups = deque(cups)
waste_water = 0
while bottles or cups:
    if cups and bottles:
        cup = cups.popleft()
        bottle = bottles.pop()
    else:
        break
    if bottle >= cup:
        waste_water += bottle - cup
    else:
        cup = cup - bottle
        while cup > 0:
            bottle = bottles.pop()
            if bottle >= cup:
                waste_water += (bottle - cup)
                cup = cup - bottle
            else:
                cup = cup - bottle
# if cups:
#     cups = [str(s) for s in cups]
#     print(f'Cups: {" ".join(cups)}')
# else:
#     bottles = [str(s) for s in bottles]
#     print(f'Bottles: {" ".join(bottles)}')
# print(f'Wasted litters of water: {waste_water}')

if cups:
    print(f'Cups: ', end='')
    print(*cups, sep=" ")
else:
    print(f'Bottle: ', end='')
    print(*bottles, sep="")
print(f'Wasted litters of water: {waste_water}')


#***
from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:
    bottle = bottles.pop()
    cup = cups.popleft() - bottle

    if cup > 0:
        cups.appendleft(cup)
    else:
        wasted_water += abs(cup)

if bottles:
    print(f'Bottles: {" ".join([str(x) for x in bottles])}')
else:
    print(f'Cups: {" ".join([str(x) for x in cups])}')

print(f'Wasted litters of water: {wasted_water}')