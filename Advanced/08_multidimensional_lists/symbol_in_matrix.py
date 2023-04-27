size = int(input())
matrix = []
for _ in range(size):
    # line = input()
    # temp = []
    # for char in line:
    #     temp.append(char)
    matrix.append(list(input()))

search_char = input()
not_found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == search_char:
            print(f'({i}, {j})')
            not_found = True
            break
    if not_found:
        break


if not not_found:
    print(f"{search_char} does not occur in the matrix")