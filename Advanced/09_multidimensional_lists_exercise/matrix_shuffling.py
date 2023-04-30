def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(s) for s in input().split()]
matrix = []
for _ in range(rows):
    line = input().split()
    matrix.append(line)
while True:
    command = input()
    if command == 'END':
        break
    elements = command.split()
    if len(elements) != 5 or elements[0] != 'swap':
        print('Invalid input!')
        continue
    elements = elements[1::]
    i, j, m, n = [int(s) for s in elements]
    if is_outside(i, j, rows, cols) or is_outside(m, n, rows, cols):
        print('Invalid input!')
        continue
    else:
        matrix[i][j], matrix[m][n] = matrix[m][n], matrix[i][j]
        for r in matrix:
            print(*r, sep=' ')