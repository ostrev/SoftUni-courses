rows, cols = [int(s) for s in input().split(', ')]
matrix = []


for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)


for col in range(cols):
    sum_mat = 0
    for row in range(rows):
        sum_mat += matrix[row][col]
    print(sum_mat)