def neib(row, col, mat):
    if row - 1 >= 0 and mat[row - 1][col] != '*':
        mat[row - 1][col] += 1
    if row + 1 < size and mat[row + 1][col] != '*':
        mat[row + 1][col] += 1
    if col + 1 < size and mat[row][col + 1] != '*':
        mat[row][col + 1] += 1
    if col - 1 >= 0 and mat[row][col - 1] != '*':
        mat[row][col - 1] += 1
    if row - 1 >= 0 and col - 1 >= 0 and mat[row - 1][col - 1] != '*':
        mat[row - 1][col - 1] += 1
    if row + 1 < size and col + 1 < size and mat[row + 1][col + 1] != '*':
        mat[row + 1][col + 1] += 1
    if row + 1 < size and col - 1 >= 0 and mat[row + 1][col - 1] != '*':
        mat[row + 1][col - 1] += 1
    if row - 1 >= 0 and col + 1 < size and mat[row - 1][col + 1] != '*':
        mat[row - 1][col + 1] += 1

size = int(input())
num_of_bombs = int(input())

matrix = []
for i in range(size):
    matrix.append([])
    for j in range(size):
        matrix[i].append(0)

for _ in range(num_of_bombs):
    bomb_row, bomb_col = eval(input())
    matrix[bomb_row][bomb_col] = '*'
    neib(bomb_row, bomb_col, matrix)


for r in matrix:
    print(' '.join([str(s) for s in r]))