from collections import deque
honey_bee = [int(s) for s in input().split()]
nectar_collected = [int(s) for s in input().split()]

honey_bee = deque(honey_bee)

symbols = deque(input().split())
honey_made = 0

while honey_bee and nectar_collected:
    bee = honey_bee[0]
    nectar = nectar_collected[-1]

    if nectar >= bee:
        bee = honey_bee.popleft()
        symbol = symbols.popleft()
        nectar_collected.pop()
        if symbol == '+':
            honey_made += bee + nectar
        elif symbol == '-':
            honey_made += abs(bee - nectar)
        elif symbol == '*':
            honey_made += abs(bee * nectar)
        elif symbol == '/':
            if nectar != 0:
                honey_made += abs(bee / nectar)

    else:
        nectar_collected.pop()


print(f'Total honey made: {honey_made}')
if honey_bee:
    print(f'Bees left: {", ".join([str(s) for s in honey_bee])}')
if nectar_collected:
    print(f'Nectar left: {", ".join([str(s) for s in nectar_collected])}')
