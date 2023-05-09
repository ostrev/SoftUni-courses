def next_position(i, j, mat, comm):
    if comm == 'up':
        if i == 0:
            i = len(mat) - 1
        else:
            i -= 1
    elif comm == 'down':
        if i == len(mat) - 1:
            i = 0
        else:
            i += 1
    elif comm == 'left':
        if j == 0:
            j = len(mat) - 1
        else:
            j -= 1
    elif comm == 'right':
        if j == len(mat) - 1:
            j = 0
        else:
            j += 1
    return i, j


size = int(input())
matrix = []
position = []
start_point = []
for roww in range(size):
    line = input().split()
    matrix.append(line)
    if 'P' in line:
        start_point = [roww, line.index('P')]
        position.append(start_point)

coins = 0
row, col = start_point
is_won = True
while coins < 100:
    command = input()
    matrix[row][col] = '0'
    row, col = next_position(row, col, matrix, command)
    if matrix[row][col].isdigit():
        coins += int(matrix[row][col])
        matrix[row][col] = 'P'
        position.append([row, col])
    else:
        position.append([row, col])
        is_won = False
        break

if is_won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {int(coins / 2)} coins.")

print(f"Your path:")
for path in position:
    print(f'{path}')



# *******************************
def calculate_position(ma, row, col):
    if row < 0:
        row = len(ma) - 1
    if col < 0:
        col = len(ma) - 1
    if row >= len(ma):
        row = 0
    if col >= len(ma):
        col = 0
    return row, col


n = int(input())

matrix = []
player_position = []

for row_index in range(n):
    row_data = input().split()
    if 'P' in row_data:
        player_position = [row_index, row_data.index('P')]
    matrix.append(row_data)

player_path = []
coins = 0
is_winner = True

player_path.append(player_position)
while coins < 100:
    command = input()
    current_row, current_col = player_position
    if command == "up":
        row, col = calculate_position(matrix, current_row-1, current_col)
    elif command == "down":
        row, col = calculate_position(matrix, current_row+1, current_col)
    elif command == "right":
        row, col = calculate_position(matrix, current_row, current_col+1)
    elif command == "left":
        row, col = calculate_position(matrix, current_row, current_col-1)

    # TODO refactor repetative code
    matrix[current_row][current_col] = '0'
    if matrix[row][col] == "X":
        player_path.append([row, col])
        is_winner = False
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break
    coins += int(matrix[row][col])
    matrix[row][col] = 'P'
    player_position = [row, col]
    player_path.append(player_position)


if is_winner:
    print(f"You won! You've collected {coins} coins.")

print("Your path:")
[print(step) for step in player_path]

