def valid_position(check_row, check_col, check_matrix):
    if 0 <= check_row < len(check_matrix) and 0 <= check_col < len(check_matrix[check_row]):
        return True
    return False


def next_position(next_position_row, next_position_col, next_position_matrix):
    if next_position_matrix[next_position_row][next_position_col] == ' ':
        return True
    return False


def is_last_move(out_row, out_col, out_matrix, size):
    if out_row == 0 or out_row == size - 1 or out_col == 0 or out_col == len(out_matrix[out_row]) - 1:
        return True
    return False


def find_next_position(find_row, find_col, find_matrix, is_get_out):
    # row - 1, col UP
    if valid_position(find_row - 1, find_col, find_matrix):
        if next_position(find_row - 1, find_col, find_matrix):
            find_matrix[find_row - 1][find_col] = 'k'
            next_found_row = find_row - 1
            next_found_col = find_col
            is_get_out = True
            return next_found_row, next_found_col, is_get_out
    # row, col - 1 LEFT
    if valid_position(find_row, find_col - 1, find_matrix):
        if next_position(find_row, find_col - 1, find_matrix):
            find_matrix[find_row][find_col - 1] = 'k'
            next_found_row = find_row
            next_found_col = find_col - 1
            is_get_out = True
            return next_found_row, next_found_col, is_get_out
    # row, col + 1 RIGHT
    if valid_position(find_row, find_col + 1, find_matrix):
        if next_position(find_row, find_col + 1, find_matrix):
            find_matrix[find_row][find_col + 1] = 'k'
            next_found_row = find_row
            next_found_col = find_col + 1
            is_get_out = True
            return next_found_row, next_found_col, is_get_out
    # row + 1, col DOWN
    if valid_position(find_row + 1, find_col, find_matrix):
        if next_position(find_row + 1, find_col, find_matrix):
            find_matrix[find_row + 1][find_col] = 'k'
            next_found_row = find_row + 1
            next_found_col = find_col
            is_get_out = True
            return next_found_row, next_found_col, is_get_out

    return find_row, find_col, is_get_out


number_of_maze = int(input())
matrix = []

# insert matrix
for line in range(number_of_maze):
    matrix.append(list(input()))

# find Kate's position
current_row_position = 0
current_col_position = 0
for row in range(number_of_maze):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'k':
            current_row_position = row
            current_col_position = col

count = 0
get_out = False
while True:
    next_row, next_col, get_out = find_next_position(current_row_position, current_col_position, matrix, get_out)
    count += 1
    if get_out:
        current_row_position = next_row
        current_col_position = next_col
        get_out = False
    else:
        if is_last_move(current_row_position, current_col_position, matrix, number_of_maze):
            print(f'Kate got out in {count} moves')
            break
        else:
            print('Kate cannot get out')
            break
