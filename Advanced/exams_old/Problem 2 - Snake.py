def is_outside(i, j, s, com):
    if com == 'up':
        if i - 1 < 0:
            return True
    elif com == 'down':
        if i + 1 >= s:
            return True
    elif com == 'left':
        if j - 1 < 0:
            return True
    elif com == 'right':
        if j + 1 >= s:
            return True


def next_position(i, j, com):
    if com == 'up':
        i -= 1
    elif com == 'down':
        i += 1
    elif com == 'left':
        j -= 1
    elif com == 'right':
        j += 1
    return i, j


size = int(input())

matrix = []
snake_row = 0
snake_col = 0
burrow_position = []
for row in range(size):
    line = list(input())
    matrix.append(line)
    if 'S' in line:
        snake_row = row
        snake_col = line.index('S')
    if 'B' in line:
        burrow_position.append([row, line.index('B')])
food_quantity = 0

game_over = False

while True:
    command = input()
    matrix[snake_row][snake_col] = '.'

    if is_outside(snake_row, snake_col, size, command):
        game_over = True
        break

    next_row, next_col = next_position(snake_row, snake_col, command)

    if matrix[next_row][next_col] == 'B':
        matrix[next_row][next_col] = '.'
        position_one_r, position_one_c = burrow_position[0]
        position_two_r, position_two_c = burrow_position[1]
        if next_row == position_one_r and next_col == position_one_c:
            next_row = position_two_r
            next_col = position_two_c
        else:
            next_row = position_one_r
            next_col = position_one_c

    elif matrix[next_row][next_col] == '*':
        food_quantity += 1

    matrix[next_row][next_col] = 'S'

    snake_row = next_row
    snake_col = next_col
    if food_quantity == 10:
        break

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")

for row in matrix:
    print(f'{"".join(row)}')
