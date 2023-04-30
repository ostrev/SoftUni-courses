def next_position(command, row, col):
    if command == 'U':
        return row - 1, col
    if command == 'D':
        return row + 1, col
    if command == 'R':
        return row, col + 1
    if command == 'L':
        return row, col - 1


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(s) for s in input().split()]

matrix = []
player_row = 0
player_col = 0
bunnies = set()
for row in range(rows):
    line = list(input())
    matrix.append(line)
    for col in range(cols):
        if line[col] == 'P':
            player_row = row
            player_col = col
        elif line[col] == 'B':

            bunnies.add((row, col))
commands = input()
is_won = False
is_dead = False
matrix[player_row][player_col] = '.'
for command in commands:
    next_row, next_col = next_position(command, player_row, player_col)

    if is_outside(next_row, next_col, rows, cols):
        is_won = True
    elif matrix[next_row][next_col] == 'B':
        is_dead = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col
    temp_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = bunny[0], bunny[1]

        if not is_outside(bunny_row - 1, bunny_col, rows, cols):
            temp_bunnies.add((bunny_row - 1, bunny_col))
            matrix[bunny_row - 1][bunny_col] = 'B'
        if not is_outside(bunny_row + 1, bunny_col, rows, cols):
            temp_bunnies.add((bunny_row + 1, bunny_col))
            matrix[bunny_row + 1][bunny_col] = 'B'
        if not is_outside(bunny_row, bunny_col + 1, rows, cols):
            temp_bunnies.add((bunny_row, bunny_col + 1))
            matrix[bunny_row][bunny_col + 1] = 'B'
        if not is_outside(bunny_row, bunny_col - 1, rows, cols):
            temp_bunnies.add((bunny_row, bunny_col - 1))
            matrix[bunny_row][bunny_col - 1] = 'B'

    bunnies = bunnies.union(temp_bunnies)
    if matrix[player_row][player_col] == 'B':
        is_dead = True
    if is_won or is_dead:
        break

for row in matrix:
    print(*row, sep='')
if is_won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')