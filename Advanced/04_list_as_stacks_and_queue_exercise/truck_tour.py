from collections import deque
number = int(input())

queue = deque()
for _ in range(number):
    station = input().split()
    station = [int(s) for s in station]
    queue.append(station)

tank_gas = 0
for i in range(number):
    is_valid = False
    for m in range(number):
        tank_gas += queue[m][0]
        dist = queue[m][1]
        if tank_gas >= dist:
            tank_gas -= dist
            if number == m + 1:
                is_valid = True
        else:
            tank_gas = 0
            break
    if is_valid:
        print(i)
        break
    queue.rotate(-1)

# ***************
from collections import deque
pumps_num = int(input())

amount_petrol = []
distance = []

for _ in range(pumps_num):
    command = [int(i) for i in input().split()]
    amount_petrol.append(command[0])
    distance.append(command[1])

cycle = pumps_num
tank = 0
station = 0
petrol = deque(amount_petrol)
kilometers = deque(distance)
n = 1
while cycle:
    tank += petrol.popleft()
    dis = kilometers.popleft()
    if tank >= dis:
        cycle -= 1
        tank -= dis

    else:
        station += 1
        petrol = deque(amount_petrol)
        kilometers = deque(distance)
        petrol.rotate(-1 * n)
        kilometers.rotate(-1 * n)
        cycle = pumps_num
        tank = 0
        n += 1

print(station)

