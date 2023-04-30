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


number = int(input())
size = int(input())

matrix = []
santa_row = 0
santa_col = 0
total_nice_kids = 0
nice_kids_presents = 0

for row in range(size):
    line = input().split()
    matrix.append(line)
    for col in range(size):
        if matrix[row][col] == 'S':
            santa_row = row
            santa_col = col
        if matrix[row][col] == 'V':
            total_nice_kids += 1

while True:
    command = input()

    if command == 'Christmas morning':
        break
    next_row, next_col = get_next_position(command, santa_row, santa_col)

    if not is_valid(next_row, next_col, size):
        continue
    matrix[santa_row][santa_col] = '-'
    santa_row = next_row
    santa_col = next_col

    if matrix[santa_row][santa_col] == 'X':
        matrix[santa_row][santa_col] = 'S'

    elif matrix[santa_row][santa_col] == 'V':
        matrix[santa_row][santa_col] = 'S'
        nice_kids_presents += 1
        number -= 1

    elif matrix[santa_row][santa_col] == 'C':
        matrix[santa_row][santa_col] = 'S'
        # left row, col - 1
        if matrix[santa_row][santa_col - 1] != '-':
            if matrix[santa_row][santa_col - 1] == 'V':
                nice_kids_presents += 1
            number -= 1
            matrix[santa_row][santa_col - 1] = '-'
            if number == 0:
                break
        # right row, col + 1
        if matrix[santa_row][santa_col + 1] != '-':
            if matrix[santa_row][santa_col + 1] == 'V':
                nice_kids_presents += 1
            number -= 1
            matrix[santa_row][santa_col + 1] = '-'
            if number == 0:
                break
        #up row - 1, col
        if matrix[santa_row - 1][santa_col] != '-':
            if matrix[santa_row - 1][santa_col] == 'V':
                nice_kids_presents += 1
            number -= 1
            matrix[santa_row - 1][santa_col] = '-'
            if number == 0:
                break
        #down row + 1, col
        if matrix[santa_row + 1][santa_col] != '-':
            if matrix[santa_row + 1][santa_col] == 'V':
                nice_kids_presents += 1
            number -= 1
            matrix[santa_row + 1][santa_col] = '-'
            if number == 0:
                break
    else:
        matrix[santa_row][santa_col] = 'S'
    if number == 0:
        break

if number == 0 and nice_kids_presents < total_nice_kids:
    print(f'Santa ran out of presents!')

for i in matrix:
    print(*i, sep=" ")

if nice_kids_presents == total_nice_kids:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_presents} nice kid/s.")
