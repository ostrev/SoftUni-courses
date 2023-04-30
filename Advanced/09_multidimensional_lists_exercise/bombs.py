from collections import deque


def is_inside(i, j, size):
    return 0 <= i < size and 0 <= j < size


def get_neighbours(i, j, size):
    # i - 1, j
    if is_inside(i - 1, j, size) and matrix[i - 1][j] > 0:
        neighbours.append([i - 1, j])
    # i + 1, j
    if is_inside(i + 1, j, size) and matrix[i + 1][j] > 0:
        neighbours.append([i + 1, j])
    # i, j - 1
    if is_inside(i, j - 1, size) and matrix[i][j - 1] > 0:
        neighbours.append([i, j - 1])
    # i, j + 1
    if is_inside(i, j + 1, size) and matrix[i][j + 1] > 0:
        neighbours.append([i, j + 1])
    # i + 1, j + 1
    if is_inside(i + 1, j + 1, size) and matrix[i + 1][j + 1] > 0:
        neighbours.append([i + 1, j + 1])
    # i - 1, j - 1
    if is_inside(i - 1, j - 1, size) and matrix[i - 1][j - 1] > 0:
        neighbours.append([i - 1, j - 1])
    # i + 1, j - 1
    if is_inside(i + 1, j - 1, size) and matrix[i + 1][j - 1] > 0:
        neighbours.append([i + 1, j - 1])
    # i - 1, j + 1
    if is_inside(i - 1, j + 1, size) and matrix[i - 1][j + 1] > 0:
        neighbours.append([i - 1, j + 1])
    return neighbours


neighbours = []
size = int(input())

matrix = []

for _ in range(size):
    line = [int(s) for s in input().split()]
    matrix.append(line)

bombs_indexes = deque(input().split())

while bombs_indexes:

    row, col = [int(s) for s in bombs_indexes.popleft().split(',')]

    if matrix[row][col] <= 0:
        continue

    reduce_value = matrix[row][col]
    matrix[row][col] = 0

    neighbours = get_neighbours(row, col, size)

    for row, col in neighbours:
        matrix[row][col] -= reduce_value
    neighbours.clear()


alive = []
for i in range(size):
    for j in range(size):
        if matrix[i][j] > 0:
            alive.append(matrix[i][j])
print(f'Alive cells: {len(alive)}')
print(f'Sum: {sum(alive)}')
for r in matrix:
    print(*r, sep=' ')