command = input()
dwarfs = {}
hat_name = {}
new_dwarfs = {}
while command != 'Once upon a time':
    name, hat_color, physics = command.split(' <:> ')
    color_name = f'({hat_color}) {name}'
    physics = int(physics)

    if hat_color not in hat_name:
        hat_name[hat_color] = [name]
    else:
        if name not in hat_name[hat_color]:
            hat_name[hat_color].append(name)

    if color_name not in dwarfs:
        dwarfs[color_name] = physics
    else:
        if physics > dwarfs[color_name]:
            dwarfs[color_name] = physics

    command = input()
sort_hat_name = sorted(hat_name.items(), key=lambda x: len(x[1]), reverse=True)


for color, names in sort_hat_name:
    for name in names:
        dr = f"({color}) {name}"
        new_dwarfs[dr] = dwarfs[dr]

for k, v in sorted(new_dwarfs.items(), key=lambda kvpt: -kvpt[1]):
    print(f'{k} <-> {v}')