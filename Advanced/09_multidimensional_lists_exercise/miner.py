def find_start_position(matrix):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 's':
                return row, col


def find_coal(c, matrix):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'c':
                c += 1
    return c


def is_outside(row, col, size):
    return row >= size or col >= size or row < 0 or col < 0


def next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'right':
        return row, col + 1
    if command == 'left':
        return row, col - 1


size = int(input())
commands = input().split()
coal = 0
matrix = []

for _ in range(size):
    line = input().split()
    matrix.append(line)

i, j = find_start_position(matrix)
matrix[i][j] = '*'
coal = find_coal(coal, matrix)
is_end = False
for command in commands:

    next_row, next_col = next_position(command, i, j)

    if is_outside(next_row, next_col, size):
        continue

    i, j = next_row, next_col

    if matrix[i][j] == 'c':
        coal -= 1
        matrix[i][j] = '*'
        if coal > 0:
            continue
        else:
            print(f"You collected all coal! ({i}, {j})")
            is_end = True
    if matrix[i][j] == 'e':
        print(f"Game over! ({i}, {j})")
        is_end = True

if not is_end:
    print(f'{coal} pieces of coal left. ({i}, {j})')


