junk = {}
key_materials = {'motes': 0, 'fragments': 0, 'shards': 0}
is_brake = False
while True:
    input_line = input().lower().split()

    for i in range(0, len(input_line), 2):
        item = input_line[i + 1]
        quantity = int(input_line[i])

        if item == 'shards' or item == 'fragments' or item == 'motes':

            if item not in key_materials:
                key_materials[item] = quantity
            else:
                key_materials[item] += quantity

            if key_materials[item] >= 250:
                is_brake = True
                if item == 'shards':
                    legendary_item = 'Shadowmourne'
                    key_materials[item] -= 250
                elif item == 'fragments':
                    legendary_item = 'Valanyr'
                    key_materials[item] -= 250
                elif item == 'motes':
                    legendary_item = 'Dragonwrath'
                    key_materials[item] -= 250
                print(f'{legendary_item} obtained!')

                break
        else:
            if item not in junk:
                junk[item] = quantity
            else:
                junk[item] += quantity
    if is_brake:
        break

sorted_key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
for k, v in sorted_key_materials.items():
    print(f'{k}: {v}')

sorted_junk = dict(sorted(junk.items(), key=lambda x: x[0]))
for k, v in sorted_junk.items():
    print(f'{k}: {v}')
