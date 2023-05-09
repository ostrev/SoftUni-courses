import copy


def get_magic_triangle(num):
    magic = []
    temp_row = []
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            temp_row.append(1)
        temp = copy.deepcopy(temp_row)
        magic.append(temp)
        temp_row.clear()

    for i in range(2, num):
        for j in range(1, i):
            magic[i][j] = magic[i - 1][j] + magic[i - 1][j - 1]

    return magic


get_magic_triangle(5)
