from collections import deque
materials = [int(s) for s in input().split()]
magic_level = [int(s) for s in input().split()]
magic_level = deque(magic_level)


craft_presents = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while materials and magic_level:
    material = materials[-1]
    magic = magic_level[0]

    if material == 0:
        materials.pop()
    if magic == 0:
        magic_level.popleft()
    if magic * material == 150:
        craft_presents['Doll'] += 1
        materials.pop()
        magic_level.popleft()
    elif magic * material == 250:
        craft_presents['Wooden train'] += 1
        materials.pop()
        magic_level.popleft()
    elif magic * material == 300:
        craft_presents['Teddy bear'] += 1
        materials.pop()
        magic_level.popleft()
    elif magic * material == 400:
        craft_presents['Bicycle'] += 1
        materials.pop()
        magic_level.popleft()

    elif magic * material < 0:
        value = magic + material
        materials.pop()
        magic_level.popleft()
        materials.append(value)
    elif magic * material > 0:
        magic_level.popleft()
        materials[-1] += 15

if craft_presents['Doll'] > 0 and craft_presents['Wooden train'] > 0 or craft_presents['Teddy bear'] > 0 and craft_presents['Bicycle'] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(i) for i in reversed(materials)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(i) for i in magic_level])}")

craft_presents_sort = sorted(craft_presents.items(), key=lambda kvpt: kvpt[0])

for key, value in craft_presents_sort:
    if value > 0:
        print(f'{key}: {value}')