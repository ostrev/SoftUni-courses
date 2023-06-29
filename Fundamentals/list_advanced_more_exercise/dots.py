def is_inside(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def get_neighbours_dots(row, col, matrix, rows, cols, visit_dots):
    neighbours = set()
    if is_inside(row + 1, col, rows, cols) and matrix[row + 1][col] == '.' and (row + 1, col) not in visit_dots:
        neighbours.add((row + 1, col))
    if is_inside(row - 1, col, rows, cols) and matrix[row - 1][col] == '.' and (row - 1, col) not in visit_dots:
        neighbours.add((row - 1, col))
    if is_inside(row, col + 1, rows, cols) and matrix[row][col + 1] == '.' and (row, col + 1) not in visit_dots:
        neighbours.add((row, col + 1))
    if is_inside(row, col - 1, rows, cols) and matrix[row][col - 1] == '.' and (row, col - 1) not in visit_dots:
        neighbours.add((row, col - 1))
    return neighbours


rows_count = int(input())

cols_count = 0
visited_dots = []
board = []

for row_index in range(rows_count):
    row_elements = input().split()
    board.append(row_elements)
    cols_count = len(row_elements)

max_counter = 0

for row_index in range(rows_count):
    for column_index in range(cols_count):
        current_count = 0
        if board[row_index][column_index] == '.':
            current_count += 1
            visited_dots.append((row_index, column_index))
            neighbours_dots = get_neighbours_dots(row_index, column_index, board, rows_count, cols_count, visited_dots)
            while neighbours_dots:
                current_count += 1
                row_i, col_i = neighbours_dots.pop()
                visited_dots.append((row_i, col_i))
                new_neighbours = get_neighbours_dots(row_i, col_i, board, rows_count, cols_count, visited_dots)
                neighbours_dots = neighbours_dots.union(new_neighbours)
            if current_count > max_counter:
                max_counter = current_count

print(max_counter)
