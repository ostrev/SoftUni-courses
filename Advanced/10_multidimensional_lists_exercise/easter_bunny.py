def get_sum(row, col, matrix):
    next_col_r = col + 1
    next_col_l = col - 1
    next_row_d = row + 1
    next_row_u = row - 1
    right_sum = 0
    left_sum = 0
    down_sum = 0
    up_sum = 0
    max_sum = -1
    end_row = 0
    end_col = 0
    direction = ''
    while is_inside(row, next_col_r, size) and matrix[row][next_col_r] != 'X':
        value = int(matrix[row][next_col_r])
        right_sum += value
        next_col_r += 1
    if right_sum > max_sum:
        max_sum = right_sum
        end_row = row
        end_col = next_col_r - 1
        direction = 'right'

    while is_inside(row, next_col_l, size) and matrix[row][next_col_l] != 'X':
        value = int(matrix[row][next_col_l])
        left_sum += value
        next_col_l -= 1
    if left_sum > max_sum:
        max_sum = left_sum
        end_row = row
        end_col = next_col_l + 1
        direction = 'left'

    while is_inside(next_row_d, col, size) and matrix[next_row_d][col] != 'X':
        value = int(matrix[next_row_d][col])
        down_sum += value
        next_row_d += 1
    if down_sum > max_sum:
        max_sum = down_sum
        end_row = next_row_d - 1
        end_col = col
        direction = 'down'

    while is_inside(next_row_u, col, size) and matrix[next_row_u][col] != 'X':
        value = int(matrix[next_row_u][col])
        up_sum += value
        next_row_u -= 1
    if up_sum > max_sum:
        max_sum = up_sum
        end_row = next_row_u + 1
        end_col = col
        direction = 'up'

    return max_sum, end_row, end_col, direction


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())

matrix = []
bunny_row = 0
bunny_col = 0

for row in range(size):
    line = input().split()
    matrix.append(line)
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny_row = row
            bunny_col = col

max_sum, end_row, end_col, direction = get_sum(bunny_row, bunny_col, matrix)
print(direction)
if direction == 'right':
    for i in range(bunny_col + 1, end_col + 1):
        print(f'[{end_row}, {i}]')
elif direction == 'left':
    for i in range(bunny_col - 1, end_col - 1, -1):
        print(f'[{end_row}, {i}]')
elif direction == 'down':
    for i in range(bunny_row + 1, end_row + 1):
        print(f'[{i}, {end_col}]')
elif direction == 'up':
    for i in range(bunny_row - 1, end_row - 1, -1):
        print(f'[{i}, {end_col}]')
print(max_sum)

# print(end_row)
# print(end_col)
