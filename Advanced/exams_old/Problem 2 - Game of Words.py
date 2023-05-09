def next_move(i, j, comm, is_out):
    is_out = False
    if comm == 'up':
        if (i - 1) < 0: # IS OUTSIDE
            is_out = True
            return i, j, is_out
        else:
            i -= 1
            return i, j, is_out
    elif comm == "down":
        if (i + 1) >= size:  # IS OUTSIDE
            is_out = True
            return i, j, is_out
        else:
            i += 1
            return i, j, is_out
    elif comm == "left":
        if (j - 1) < 0:  # IS OUTSIDE
            is_out = True
            return i, j, is_out
        else:
            j -= 1
            return i, j, is_out
    elif comm == "right":
        if (j + 1) >= size:  # IS OUTSIDE
            is_out = True
            return i, j, is_out
        else:
            j += 1
            return i, j, is_out


initial_sting = input()

size = int(input())

matrix = []
position = []
for row_i in range(size):
    line = list(input())
    if 'P' in line:
        position.append(row_i)
        position.append(line.index('P'))
    matrix.append(line)

row, col = position

num_commands = int(input())
is_outside = False
for _ in range(num_commands):
    matrix[row][col] = '-'
    command = input()
    row, col, is_outside = next_move(row, col, command, is_outside)
    if is_outside:
        if initial_sting:
            initial_sting = initial_sting[:-1]
        matrix[row][col] = "P"
    else:
        if matrix[row][col] != '-':
            initial_sting += matrix[row][col]
            matrix[row][col] = "P"
        else:
            matrix[row][col] = "P"

print(initial_sting)
for r in matrix:
    print(''.join(r))
