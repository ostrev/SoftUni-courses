matrix = []
king_row = 0
king_col = 0
queens_list = []

for row in range(8):
    matrix.append(input().split())
    for col in range(8):
        if matrix[row][col] == 'K':
            king_row = row
            king_col = col

i = king_row
j = king_col
while i > 0:  # Check up
    i -= 1
    j = king_col
    if i >= 0 and matrix[i][j] == 'Q':
        queen_position = [i, j]
        queens_list.append(queen_position)
        break

i = king_row
j = king_col
while i < 7:  # Check down
    i += 1
    j = king_col
    if i <= 7 and matrix[i][j] == 'Q':
        queen_position = [i, j]
        queens_list.append(queen_position)
        break

i = king_row
j = king_col
while j < 7:  # Check right
    i = king_row
    j += 1
    if j <= 7 and matrix[i][j] == 'Q':
        queen_position = [i, j]
        queens_list.append(queen_position)
        break

i = king_row
j = king_col
while j > 0:  # Check left
    i = king_row
    j -= 1
    if j >= 0 and matrix[i][j] == 'Q':
        queen_position = [i, j]
        queens_list.append(queen_position)
        break

i = king_row
j = king_col
while i > 0 and j < 7:  # Check up right
    i -= 1
    j += 1
    if i >= 0 and j <= 7 and matrix[i][j] == 'Q':
        queen_position = [i, j]
        queens_list.append(queen_position)
        break

i = king_row
j = king_col
while i > 0 and j > 0:  # Check up left
    i -= 1
    j -= 1
    if i >= 0 and j >= 0 and matrix[i][j] == 'Q':
        queen_position = [i, j]
        queens_list.append(queen_position)
        break

i = king_row
j = king_col
while i < 7 and j < 7:  # Check down right
    i += 1
    j += 1
    if i <= 7 and j <= 7 and matrix[i][j] == 'Q':
        queen_position = [i, j]
        queens_list.append(queen_position)
        break

i = king_row
j = king_col
while i < 7 and j > 0:  # Check down left
    i += 1
    j -= 1
    if i <= 7 and j >= 0 and matrix[i][j] == 'Q':
        queen_position = [i, j]
        queens_list.append(queen_position)
        break


if queens_list:
    for position in queens_list:
        print(position)
else:
    print("The king is safe!")

