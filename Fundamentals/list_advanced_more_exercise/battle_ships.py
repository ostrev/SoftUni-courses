number_of_rows = int(input())
battle_field = []
for _ in range(number_of_rows):
    ships_row = [int(s) for s in input().split()]
    battle_field.append(ships_row)

attacks = []
list_of_attacks = input().split()

for index in range(len(list_of_attacks)):
    attack = list_of_attacks[index].split('-')
    attacks.append([int(s) for s in attack])
count = 0
while len(attacks) > 0:
    ship_row_attacked = attacks[0][0]
    ship_col_attacked = attacks[0][1]
    if battle_field[ship_row_attacked][ship_col_attacked] != 0:
        battle_field[ship_row_attacked][ship_col_attacked] -= 1
        if battle_field[ship_row_attacked][ship_col_attacked] == 0:
            count += 1
    attacks.pop(0)

print(count)