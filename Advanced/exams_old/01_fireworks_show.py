from collections import deque as dq

firework_effects = dq(int(i) for i in input().split(', '))
explosive_power = [int(i) for i in input().split(', ')]

result_fireworks = {'Palm Fireworks': 0,
                    'Willow Fireworks': 0,
                    'Crossette Fireworks': 0}
is_made = False

while firework_effects and explosive_power:
    firework = firework_effects[0]
    explosive = explosive_power[-1]
    if firework <= 0:
        firework_effects.popleft()
        continue
    if explosive <= 0:
        explosive_power.pop()
        continue

    result = firework + explosive

    if result % 3 == 0 and result % 5 != 0:
        result_fireworks['Palm Fireworks'] += 1

    elif result % 3 != 0 and result % 5 == 0:
        result_fireworks['Willow Fireworks'] += 1
    elif result % 3 == 0 and result % 5 == 0:
        result_fireworks['Crossette Fireworks'] += 1
    else:
        firework_effects.append(firework - 1)
        explosive_power.append(explosive)

    firework_effects.popleft()
    explosive_power.pop()

    if result_fireworks['Palm Fireworks'] >= 3 and result_fireworks['Willow Fireworks'] >= 3 \
            and result_fireworks['Crossette Fireworks'] >= 3:
        is_made = True
        break

if is_made:
    print('Congrats! You made the perfect firework show!')

else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(i) for i in firework_effects)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(i) for i in explosive_power)}")

for k, v in result_fireworks.items():
    print(f"{k}: {v}")

