# "{type} {name} {damage} {health} {armor}".
# Gold Traxx 500 null 0
def default(data):
    type_dragon, name, damage, hp, armor = data.split()
    if damage == "null":
        damage = 45
    if hp == "null":
        hp = 250
    if armor == "null":
        armor = 10
    return type_dragon, name, int(damage), int(hp), int(armor)


def avg_calculator(some_dict):
    some_list = [0, 0, 0]
    for some_key in some_dict.keys():
        some_list[0] += some_dict[some_key][0]
        some_list[1] += some_dict[some_key][1]
        some_list[2] += some_dict[some_key][2]
    for _ in range(len(some_list)):
        some_list[_] /= len(some_dict.keys())
    return some_list


count_of_dragons = int(input())
dragons = {}

for _ in range(count_of_dragons):
    data = input()
    type_dragon, name, dmg, hp, armor = default(data)
    if type_dragon not in dragons:
        dragons[type_dragon] = {}
    if name in dragons[type_dragon]:
        dragons[type_dragon][name] = []
    dragons[type_dragon][name] = [dmg, hp, armor]

for t, d in dragons.items():
    stats = avg_calculator(d)
    print(f"{t}::({stats[0]:.2f}/{stats[1]:.2f}/{stats[2]:.2f})")
    for dragon, s in sorted(d.items()):
        print(f"-{dragon} -> damage: {s[0]}, health: {s[1]}, armor: {s[2]}")