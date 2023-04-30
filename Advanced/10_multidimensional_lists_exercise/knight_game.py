def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def is_knight(row, col, matrix):
    if matrix[row][col] == 'K':
        return True
    else:
        return False


def collision(row, col, matrix):
    result = 0
    # row - 2, col - 1
    if is_inside(row - 2, col - 1, size) and is_knight(row - 2, col - 1, matrix):
        result += 1
    # row - 2, col + 1
    if is_inside(row - 2, col + 1, size) and is_knight(row - 2, col + 1, matrix):
        result += 1
    # row - 1, col - 2
    if is_inside(row - 1, col - 2, size) and is_knight(row - 1, col - 2, matrix):
        result += 1
    # row - 1, col + 2
    if is_inside(row - 1, col + 2, size) and is_knight(row - 1, col + 2, matrix):
        result += 1
    # row + 2, col - 1
    if is_inside(row + 2, col - 1, size) and is_knight(row + 2, col - 1, matrix):
        result += 1
    # row + 2, col + 1
    if is_inside(row + 2, col + 1, size) and is_knight(row + 2, col + 1, matrix):
        result += 1
    # row + 1, col - 2
    if is_inside(row + 1, col - 2, size) and is_knight(row + 1, col - 2, matrix):
        result += 1
    # row + 1, col + 2
    if is_inside(row + 1, col + 2, size) and is_knight(row + 1, col + 2, matrix):
        result += 1
    return result

size = int(input())

matrix = []
remove_knights = 0
for _ in range(size):
    line = list(input())
    matrix.append(line)

while True:
    dict = {}
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == '0':
                continue
            counter = collision(i, j, matrix)
            if counter:
                dict[(i, j)] = counter

    if len(dict) == 0:
        break

    sort_dict = sorted(dict.items(), key = lambda kvpt: -kvpt[1])
    for key, value in sort_dict:
        n, m = key
        matrix[int(n)][int(m)] = '0'
        remove_knights += 1
        break

print(remove_knights)