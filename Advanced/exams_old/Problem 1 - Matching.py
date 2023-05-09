from collections import deque as dq

males = [int(s) for s in input().split()]
females = dq([int(s) for s in input().split()])
count = 0
while males and females:
    pass
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue
    if female <= 0:
        females.popleft()
        continue

    if male % 25 == 0:
        males.pop()
        males.pop()
        continue
    if female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if male == female:
        count +=1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {count}")
if males:
    print(f'Males left: {", ".join([str(s) for s in reversed(males)])}')
else:
    print('Males left: none')

if females:
    print(f'Females left: {", ".join([str(s) for s in females])}')
else:
    print('Females left: none')