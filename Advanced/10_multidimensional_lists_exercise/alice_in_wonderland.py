def get_next_position(command, row, col):
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'up':
        return row - 1, col
    return row + 1, col


def is_valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    else:
        return False


size = int(input())

matrix = []
alice_row = 0
alice_col = 0
tea_sum = 0
for row in range(size):
    line = input().split()
    matrix.append(line)
    for col in range(size):
        if matrix[row][col] == 'A':
            alice_row = row
            alice_col = col
matrix[alice_row][alice_col] = '*'

while True:
    command = input()
    next_row, next_col = get_next_position(command, alice_row, alice_col)

    if not is_valid(next_row, next_col, size):
        break
    if matrix[next_row][next_col] == 'R':
        matrix[next_row][next_col] = '*'
        break

    alice_row = next_row
    alice_col = next_col
    value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = '*'

    if value.isdigit():
        tea_sum += int(value)
        if tea_sum >= 10:
            break
if tea_sum >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=' ')
