from collections import deque
def get_next_position(command, row, col, step):
    if command == 'left':
        return row, col - step
    if command == 'right':
        return row, col + step
    if command == 'up':
        return row - step, col
    return row + step, col


def get_target(command, row, col, matrix, is_shoot):
    is_shoot = False
    if command == 'left' and col > 0:
        for i in range(col-1, -1, -1):
            if matrix[row][i] == 'x':
                col = i
                is_shoot = True
                break
    if command == 'right' and col < size:
        for i in range(col + 1, size):
            if matrix[row][i] == 'x':
                col = i
                is_shoot = True
                break
    if command == 'up' and row > 0:
        for i in range(row - 1, -1, -1):
            if matrix[i][col] == 'x':
                row = i
                is_shoot = True
                break
    if command == 'down' and row < size:
        for i in range(row + 1, size):
            if matrix[i][col] == 'x':
                row = i
                is_shoot = True
                break

    return row, col, is_shoot


def is_valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    else:
        return False


size = 5

matrix = []
shoot_row = 0
shoot_col = 0
targets = deque([])
counter_targets = 0

for row in range(size):
    line = input().split()
    matrix.append(line)
    for col in range(size):
        if matrix[row][col] == 'A':
            shoot_row = row
            shoot_col = col
        if matrix[row][col] == 'x':
            counter_targets += 1
all_targets = counter_targets

number = int(input())




for _ in range(number):
    command = input().split()
    if command[0] == 'move':
        next_row, next_col = get_next_position(command[1], shoot_row, shoot_col, int(command[2]))
        if not is_valid(next_row, next_col, size): # da e razlichno ot X i da smenq A s .
            continue
        if matrix[next_row][next_col] != '.':
            continue
        matrix[shoot_row][shoot_col] = '.'
        shoot_row = next_row
        shoot_col = next_col
        matrix[shoot_row][shoot_col] = 'A'
    else:
        is_shoot = False
        target_row, target_col, is_shoot = get_target(command[1], shoot_row, shoot_col, matrix, is_shoot)
        if is_shoot:
            targets.append((target_row, target_col))
            counter_targets -= 1
            matrix[target_row][target_col] = '.'
        if counter_targets == 0:
            break

if counter_targets == 0:
    print(f'Training completed! All {all_targets} targets hit.')
else:
    print(f'Training not completed! {counter_targets} targets left.')

while targets:
    value = targets.popleft()
    print(f'[{value[0]}, {value[1]}]')


#********************************
def get_next_position(command, row, col, step=1):
    if command == 'left':
        return row, col - step
    if command == 'right':
        return row, col + step
    if command == 'up':
        return row - step, col
    return row + step, col


def is_valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    else:
        return False


size = 5

matrix = []
shoot_row = 0
shoot_col = 0
targets = []
counter_targets = 0

for row in range(size):
    line = input().split()
    matrix.append(line)
    for col in range(size):
        if matrix[row][col] == 'A':
            shoot_row = row
            shoot_col = col
        if matrix[row][col] == 'x':
            counter_targets += 1
all_targets = counter_targets

number = int(input())


for _ in range(number):
    command = input().split()
    if command[0] == 'move':
        next_row, next_col = get_next_position(command[1], shoot_row, shoot_col, int(command[2]))
        if not is_valid(next_row, next_col, size):  # da e razlichno ot X i da smenq A s .
            continue
        if matrix[next_row][next_col] != '.':
            continue
        matrix[shoot_row][shoot_col] = '.'
        shoot_row = next_row
        shoot_col = next_col
        matrix[shoot_row][shoot_col] = 'A'
    else:
        bullet_row, bullet_col = get_next_position(command[1], shoot_row, shoot_col, 1)
        while True:
            if not is_valid(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == 'x':
                counter_targets -= 1
                targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break
            bullet_row, bullet_col = get_next_position(command[1], bullet_row, bullet_col)
        if counter_targets == 0:
            break

if counter_targets == 0:
    print(f'Training completed! All {all_targets} targets hit.')
else:
    print(f'Training not completed! {counter_targets} targets left.')

for target in targets:
    print(target)