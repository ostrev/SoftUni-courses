from collections import deque as dq


def check_value(mix, gifts):
    if 100 <= mix <= 199:
        if "Gemstone" not in gifts:
            gifts['Gemstone'] = 0
        gifts['Gemstone'] += 1
    elif 200 <= mix <= 299:
        if "Porcelain Sculpture" not in gifts:
            gifts['Porcelain Sculpture'] = 0
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= mix <= 399:
        if "Gold" not in gifts:
            gifts['Gold'] = 0
        gifts['Gold'] += 1
    elif 400 <= mix <= 499:
        if "Diamond Jewellery" not in gifts:
            gifts['Diamond Jewellery'] = 0
        gifts['Diamond Jewellery'] += 1
    return gifts


gifts = {}
materials = [int(s) for s in input().split()]
magic_level = dq([int(s) for s in input().split()])

while materials and magic_level:
    first = materials.pop()
    last = magic_level.popleft()
    mix = first + last

    gifts = check_value(mix, gifts)

    if mix < 100:
        if mix % 2 == 0:
            first = 2 * first
            last = 3 * last
            mix = first + last
        else:
            mix *= 2

        gifts = check_value(mix, gifts)
    elif mix > 499:
        mix = mix/2
        gifts = check_value(mix, gifts)


if 'Gemstone' in gifts and 'Porcelain Sculpture' in gifts or 'Gold' in gifts and 'Diamond Jewellery' in gifts:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join([str(s) for s in materials])}')

if magic_level:
    print(f'Magic left: {", ".join([str(s) for s in magic_level])}')

for k, v in sorted(gifts.items()):
    print(f'{k}: {v}')
