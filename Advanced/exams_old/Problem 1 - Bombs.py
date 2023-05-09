from collections import deque as dq
effects = dq([int(s) for s in input().split(', ')])
casings = [int(s) for s in input().split(', ')]

bombs_type = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

is_succeed = False
while effects and casings:
    effect = effects[0]
    casing = casings[-1]
    sum_effect = effect + casing

    if sum_effect in bombs_type:
        effects.popleft()
        casings.pop()
        bombs[bombs_type[sum_effect]] += 1
    else:
        casings[-1] -= 5

    if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
        is_succeed = True
        break

if is_succeed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join([str(s) for s in effects])}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join([str(s) for s in casings])}")
else:
    print("Bomb Casings: empty")


for k, v in sorted(bombs.items()):
    print(f"{k}: {v}")

