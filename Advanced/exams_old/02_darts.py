size = 7
names = input().split(', ')
matrix = []
player_dict = {1: 501, 2: 501}
# player_one = 501
# player_two = 501
throws = {1: 0, 2: 0}

for row in range(size):
    matrix.append(input().split())

player_turn = 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


count = 1

while True:
    if count % 2 == 1:
        player_turn = 1
    else:
        player_turn = 2
    throw_row, throw_col = [int(i) for i in input().strip('()').split(', ')]
    if not is_inside(throw_row, throw_col, size):
        count += 1
        throws[player_turn] += 1
    else:
        if matrix[throw_row][throw_col].isdigit():
            player_dict[player_turn] -= int(matrix[throw_row][throw_col])
        elif matrix[throw_row][throw_col] == 'D':
            player_dict[player_turn] -= (sum([int(matrix[throw_row][0]), int(matrix[throw_row][-1]),
                                              int(matrix[0][throw_col]), int(matrix[size - 1][throw_col])])) * 2
        elif matrix[throw_row][throw_col] == 'T':
            player_dict[player_turn] -= (sum([int(matrix[throw_row][0]), int(matrix[throw_row][-1]),
                                              int(matrix[0][throw_col]), int(matrix[size - 1][throw_col])])) * 3
        elif matrix[throw_row][throw_col] == 'B':
            is_winner = True
            throws[player_turn] += 1
            player_dict[player_turn] = 0
            break
        throws[player_turn] += 1
        count += 1
        if player_dict[player_turn] <= 0:
            break

for k, v in player_dict.items():
    if v <= 0:
        print(f"{names[k - 1]} won the game with {throws[k]} throws!")
