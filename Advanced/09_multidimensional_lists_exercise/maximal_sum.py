import sys

rows, cols = [int(s) for s in input().split()]
matrix = []
for _ in range(rows):
    line = [int(s) for s in input().split()]
    matrix.append(line)
max_sum = -sys.maxsize
current_sum = 0
max_row = 0
max_col = 0
for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] \
                      + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + \
                      matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = i
            max_col = j

print(f'Sum = {max_sum}')

print(f'{matrix[max_row][max_col]} {matrix[max_row][max_col + 1]} {matrix[max_row][max_col + 2]}')
print(f'{matrix[max_row + 1][max_col]} {matrix[max_row + 1][max_col + 1]} {matrix[max_row + 1][max_col + 2]}')
print(f'{matrix[max_row + 2][max_col]} {matrix[max_row + 2][max_col + 1]} {matrix[max_row + 2][max_col + 2]}')
