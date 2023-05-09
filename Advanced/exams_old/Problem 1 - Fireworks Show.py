from collections import deque as dq

fireworks_effect = dq([int(s) for s in input().split(', ')])
explosive_power = [int(s) for s in input().split(', ')]
fire_dict = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

while fireworks_effect and explosive_power:

    first = fireworks_effect.popleft()
    last = explosive_power.pop()
    result = first + last
    if first <= 0:
        explosive_power.append(last)
        continue
    if last <= 0:
        fireworks_effect.appendleft(first)
        continue

    if result % 3 == 0 and result % 5 == 0:
        fire_dict['Crossette Fireworks'] += 1
    elif result % 3 == 0:
        fire_dict['Palm Fireworks'] += 1
    elif result % 5 == 0:
        fire_dict['Willow Fireworks'] += 1
    else:
        first -= 1
        fireworks_effect.append(first)
        explosive_power.append(last)

    if fire_dict['Palm Fireworks'] >= 3 and fire_dict['Willow Fireworks'] >= 3 and fire_dict[
        'Crossette Fireworks'] >= 3:
        break

if fire_dict['Palm Fireworks'] >= 3 and fire_dict['Willow Fireworks'] >= 3 and fire_dict['Crossette Fireworks'] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f"Firework Effects left: {', '.join([str(s) for s in fireworks_effect])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(s) for s in explosive_power])}")

for k, v in fire_dict.items():
    print(f"{k}: {v}")
