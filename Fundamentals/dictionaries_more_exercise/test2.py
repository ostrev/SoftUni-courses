number = int(input())
dragons = {}
physics = {'damage': 0, 'health': 0, 'armor': 0}
has_the_same_dragon = False

for i in range(number):
    type_dragon, current_name, current_damage, current_health, current_armor = input().split()
    if current_health == "null":
        current_health = 250
    else:
        current_health = int(current_health)
    if current_damage == "null":
        current_damage = 45
    else:
        current_damage = int(current_damage)
    if current_armor == "null":
        current_armor = 10
    else:
        current_armor = int(current_armor)

    physics.update({'damage': current_damage})
    physics.update({'health': current_health})
    physics.update({'armor': current_armor})

    if type_dragon not in dragons:
        dragons[type_dragon] = [{current_name: physics.copy()}]
    else:
        for index, item in enumerate(list(dragons[type_dragon])):
            for key, value in item.items():
                if key == current_name:
                    del dragons[type_dragon][index]

        dragons[type_dragon].append({current_name: physics.copy()})

for dragon_type, info in dragons.items():
    avg_damage = 0.0
    avg_health = 0.0
    avg_armor = 0.0
    length = len(info)

    for i in info:
        for name, information in i.items():
            avg_damage += information['damage']
            avg_health += information['health']
            avg_armor += information['armor']

    avg_damage = avg_damage / length
    avg_health = avg_health / length
    avg_armor = avg_armor / length

    print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    info = sorted(info, key=lambda d: list(d.keys()))

    for i in info:
        for name, information in i.items():
            print(
                f"-{name} -> damage: {information['damage']}, health: {information['health']}, armor: {information['armor']}")