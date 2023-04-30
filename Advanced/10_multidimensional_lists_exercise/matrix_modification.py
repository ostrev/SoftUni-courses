def is_valid(row, col, size):
    return row >= 0 and col >= 0 and row < size and col < size

size = int(input())
matrix = []
for _ in range(size):
    line = [int(s) for s in input().split()]
    matrix.append(line)

while True:
    commands = input()
    if commands == 'END':
        break
    command = commands.split()
    if command[0] == 'Add':
        add_row = int(command[1])
        add_col = int(command[2])
        value = int(command[3])
        if is_valid(add_row, add_col, size):
            matrix[add_row][add_col] += value
        else:
            print('Invalid coordinates')
    else:
        add_row = int(command[1])
        add_col = int(command[2])
        value = int(command[3])
        if is_valid(add_row, add_col, size):
            matrix[add_row][add_col] -= value
        else:
            print('Invalid coordinates')

for r in matrix:
    print(*r, sep=' ')